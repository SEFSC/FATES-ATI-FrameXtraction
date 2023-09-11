#!/opt/conda/bin/python3.10

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
        '-v', '--verbose',
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
    if 'window' in args and not isinstance(args.window, int):
        raise TypeError(
            'Expected type int passed to -w or --window but received '\
            f'{type(args.window).__name__}. See -h for more information.')
    if 'verbose' in args and not isinstance(args.verbose, bool):
        raise TypeError(
            'Expected type bool passed to -v or --verbose but received '\
            f'{type(args.verbose).__name__}. See -h for more information.')

    # Read in database file and reshape
    df = pd.read_csv(args.file, delimiter='\t',
                     usecols=['FilenameLeft', 'FrameLeft',
                              'FilenameRight', 'FrameRight'])
    dfNew = pd.DataFrame({
            'Filename': pd.concat((df['FilenameLeft'], df['FilenameRight'])),
            'Frame': pd.concat((df['FrameLeft'], df['FrameRight']))})
    
    # Current directory
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
                    if args.verbose:
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
                    if args.verbose:
                        print(f'...file {outFile} successfully created.\n')

        video.release()

    print('Done!')

if __name__ == '__main__':
    main()