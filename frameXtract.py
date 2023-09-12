import pandas as pd
import argparse
import cv2
import os

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        prog='frameXtract.py',
        usage='%(prog)s [arguments]',
        description='Utility to extract annotated frames from video')
    parser.add_argument(
        '-f', '--file',
        metavar='filename', type=str,
        default=argparse.SUPPRESS,
        help='Name of database file to read in. Must contain name of the '\
             'video file(s) and frame number(s) to extract. Writes to a '\
             'subdirectory "images", which is created if needed, within '\
             'the directory containing the video(s) to be processed. Image '\
             'filenames are of the form <videoFileName-frameN.jpg>, where N '\
             'is the zero-padded frame number extracted from videoFileName.')
    parser.add_argument(
        '-w', '--window',
        metavar='window', type=int,
        default=argparse.SUPPRESS,
        help='Number of frames before and after each frame in the database '\
             'to extract. For example, if set to 10, for frame 50 specified '\
             'in the database file, frames 40-60 will be extracted. '\
             'Default is 0.')
    parser.add_argument(
        '-s', '--sep',
        metavar='sep', type=str,
        default=argparse.SUPPRESS,
        help='Separator (delimiter) for database file. If omitted, the '\
             'separator will try to be determined from the file extension or '\
             'detected automatically by the Python parsing engine, but if '\
             'these both fail, this flag will be required in order to properly '\
             'read the file.')
    parser.add_argument(
        '-v', '--video',
        metavar='video', type=str,
        help='Full path to directory containing the videos to be processed. '\
             'This is only used if a full directory path is passed to "-f" '\
             'or "--file", which indicates that the program is being run '\
             'stand-alone instead of within its container. Otherwise, it '\
             'will be ignored.')
    parser.add_argument(
        '-p', '--print',
        action='store_true',
        help='Print successful reads and writes to screen.')
    return parser.parse_args()

def main():
    """MAIN PROGRAM

    Extracts frames from stereo cameras as specified in the database export
    file passed via command line (-f flag) when the program is run. Video 
    filenames and frames are both expected to be in two columns each, 
    FilenameLeft and FilenameRight, and FrameLeft and FrameRight, respectively,
    where "Left" and "Right" refer to the corresponding stereo camera.
    
    Frame numbers listed in the FrameLeft column are extracted from the
    corresponding video file in FilenameLeft, as with the right channel.
    
    Images are written to a subdirectory called "images" within the directory
    containing the video(s); this subdirectory is automatically created if it
    does not already exist. Images are saved using the file naming convention

                          <videoFileName_frameN.jpg>
    
    where N the zero-padded frame number extracted from video <videoFileName>.
    """
    # Command line arguments
    args = parse_args()

    # Sanity checks
    if 'file' not in args:
        raise NameError(
            'Database file name not found. Use -f or --file to supply a '\
            'file name. See -h for more information.')
    elif 'file' in args and not isinstance(args.file, str):
        raise TypeError(
            'Expected type str passed to -f or --file but received '\
            f'{type(args.file).__name__}. See -h for more information.')
    if 'video' in args and not isinstance(args.video, str):
        raise TypeError(
            'Expected type str passed to -v or --video but received '\
            f'{type(args.video).__name__}. See -h for more information.')
    if 'sep' in args and not isinstance(args.sep, str):
        raise TypeError(
            'Expected type str passed to -s or --sep but received '\
            f'{type(args.sep).__name__}. See -h for more information.')
    if 'window' in args and not isinstance(args.window, int):
        raise TypeError(
            'Expected type int passed to -w or --window but received '\
            f'{type(args.window).__name__}. See -h for more information.')
    if 'print' in args and not isinstance(args.print, bool):
        raise TypeError(
            'Expected type bool passed to -p or --print but received '\
            f'{type(args.print).__name__}. See -h for more information.')

    # Read in database file and reshape. Tries to determine the delimiter
    # from the file extension if not passed as a command line argument.
    # If this fails, user is prompted to specify and try again.
    if len(os.path.dirname(args.file)) > 0:
        dbFile = args.file
        container = False
        if 'video' not in args:
            raise ValueError(
                'Passing a full directory chain to "-f" or "--file" '\
                'indicates this program is being run stand-alone instead '\
                'of within its container. This requires that the video '\
                'directory be passed to "-v" or "--video", but none was '\
                'detected. See -h for more information.')
            
    else:
        dbFile = os.path.join('/home/app/annotations', args.file)
        container = True
    if 'sep' not in args:
        if args.file[-3:] == "tsv":
            args.sep = '\t'
        elif args.file[-3:] == 'csv':
            args.sep = ','
        else:
            args.sep = None
    try:
        df = pd.read_csv(dbFile, delimiter=args.sep,
                         usecols=['FilenameLeft', 'FrameLeft',
                                  'FilenameRight', 'FrameRight'])
    except ValueError:
        raise ValueError(
            f'Unable to parse the file "{args.file}" using separator '\
            f'"{args.sep}". Relaunch with the proper separator passed '\
            'to -s or --sep flag (e.g., " " for one space, ";" for '\
            'semicolon, etc., without quotations.')
    dfNew = pd.DataFrame({
            'Filename': pd.concat((df['FilenameLeft'], df['FilenameRight'])),
            'Frame': pd.concat((df['FrameLeft'], df['FrameRight']))})
    
    # Change current directory to video directory
    if container:
        os.chdir('/home/app/videos')
    else:
        os.chdir(os.path.dirname(args.video))
    pwd = os.getcwd()

    # Loop through videos listed in dataframe
    for file, group in dfNew.groupby('Filename'):

        # Make sure the file exist
        if not os.path.exists(os.path.join(pwd, file)):
            raise NameError(
                f'File "{os.path.join(pwd, file)}" cannot be found.')

        # Zero-padding and filenames
        pad = len(str(max(group['Frame'])))

        # Video capture
        video = cv2.VideoCapture(os.path.join(pwd, file))

        # Loop through frames from current video
        for dbframe in group['Frame']:

            # Create list of frames to extract if a window is supplied
            if 'window' in args:
                frames = pd.Series(pd.Series(
                    range(dbframe-args.window,
                          dbframe+args.window+1))).tolist()
            else:
                frames = [dbframe]
            
            for frame in frames:
                # Extract frame from video
                video.set(cv2.CAP_PROP_FRAME_COUNT, frame)
                flag, captured = video.read()
                if flag:
                    if args.print:
                        print(f'Frame {frame} extracted successfully from {file}...')
                else:
                    raise IndexError(
                        f'Error extracting frame {frame} from "{file}". '\
                        'Either the file could not be read or the frame '\
                        'could not be extracted. Check the video file and '\
                        'ensure the frame number does not exceed the number '\
                        'of frames in the video.')

                # Save to file
                if not os.path.exists('images'):
                    os.makedirs('images')
                filePreface = file.split('.')[0].replace(' ', '_')
                outFile = f'{filePreface}-frame{str(frame).zfill(pad)}.jpg'
                
                if not cv2.imwrite(os.path.join(pwd, 'images', outFile), captured):
                    raise Exception("Could not write image.")
                else:
                    if args.print:
                        print(f'...file {outFile} successfully created.\n')

        video.release()

    print('Done!')

if __name__ == '__main__':
    main()