import pandas as pd
import argparse
import cv2
import os

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        prog='frameXtract.py',
        usage='%(prog)s [arguments]',
        description='Utility to extract frames from video')
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
        default=argparse.SUPPRESS,
        help='Full path to directory containing the videos to be processed. '\
             'This is only used if a full directory path is passed to "-f" '\
             'or "--file", which indicates that the program is being run '\
             'stand-alone instead of within its container. Otherwise, it '\
             'will be ignored. If this is not passed but a full directory '\
             'is passed to "-f" or "--file", videos are expected to be in '\
             'the present working directory and will fail otherwise.')
    parser.add_argument(
        '-i', '--image',
        metavar='image', type=str,
        default=argparse.SUPPRESS,
        help='Full path to directory where the new images should be saved. '\
             'This is only used if a full directory path is passed to "-f" '\
             'or "--file", which indicates that the program is being run '\
             'stand-alone instead of within its container. Otherwise, it '\
             'will be ignored. If this is not passed but a full directory '\
             'is passed to "-f" or "--file", images are written to the '\
             'present working directory.')
    parser.add_argument(
        '-p', '--print',
        action='store_true',
        help='Print successful reads and writes to screen.')
    return parser.parse_args()

def getFrames(data, args, channel):
    """
    Extract the frames from channel "channel" as listed in "data".

    Input:
        data: DataFrame containing the video file names, frame numbers to
            extract, and metadata including length and fish ID
        args: argparse.Namespace object generated from command line execution
            containing user-supplied arguments
        channel: One of either "left" or "right" indicating which stereo
            channel to extract.
    """
    # Capitalize string passed to "channel" in case it isn't already
    channel = channel.title()

    # Loop through videos listed in dataframe
    for file, group in data.groupby(f'Filename{channel}'):

        # Make sure the file exists
        if not os.path.exists(os.path.join(args.video, file)):
            raise NameError(
                f'File "{os.path.join(args.video, file)}" cannot be found.')
        
        # Zero-padding for frame number in output file name
        pad = len(str(max(group[f'Frame{channel}'])))

        # Video capture
        video = cv2.VideoCapture(os.path.join(args.video, file))

        # Frames to extract from current video
        for dbframe, sample in group.drop_duplicates(subset=f'Frame{channel}',
                                                     keep=False)\
                                    .set_index(f'Frame{channel}').iterrows():
            
            # Create list of frames to extract if a window is supplied
            if hasattr(args, 'window'):
                frames = pd.Series(range(dbframe-args.window,
                                         dbframe+args.window+1)).tolist()
            else:
                frames = [dbframe]
            
            # Loop through each frame to extract from the video
            for frame in frames:
                # Extract frame from video
                video.set(cv2.CAP_PROP_POS_FRAMES, frame)
                success, captured = video.read()
                if not success:
                    raise IndexError(
                        f'Error extracting frame {frame} from {file}. '\
                        'Either the file could not be read or the frame '\
                        'could not be extracted. Check the video file and '\
                        'ensure the frame number does not exceed the number '\
                        'of frames in the video.')
                elif args.print:
                    print('Frame {} extracted successfully from {}...'\
                          .format(frame, file))

                # Output directory: ./family/genus/species/
                outPath = os.path.join(
                    args.image,
                    sample['Family'].lower(),
                    sample['Genus'].lower(),
                    sample['Species'].lower())
                if not os.path.exists(outPath):
                    print(f'Creating {outPath}')
                    os.makedirs(outPath)

                # Output filename: VideoFileName_frame-n_length-l.jpg
                #     where N = zero-padded frame number
                #           l = fish length from dataframe
                filePreface = file.split('.')[0].replace(' ', '_')
                outFile = '{}_frame-{}_length-{}.jpg'.format(
                    filePreface,
                    str(frame).zfill(pad),
                    sample['Length'])

                # Save to file
                if not cv2.imwrite(os.path.join(outPath, outFile), captured):
                    raise Exception('Could not write image.')
                elif args.print:
                    print(f'...file {outFile} successfully created.\n')

        # Close video file
        video.release()

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
    if not hasattr(args, 'file'):
        raise NameError(
            'Database file name not found. Use -f or --file to supply a '\
            'file name. See -h for more information.')
    elif hasattr(args, 'file') and not isinstance(args.file, str):
        raise TypeError(
            'Expected type str passed to -f or --file but received '\
            f'{type(args.file).__name__}. See -h for more information.')
    if hasattr(args, 'video') and not isinstance(args.video, str):
        raise TypeError(
            'Expected type str passed to -v or --video but received '\
            f'{type(args.video).__name__}. See -h for more information.')
    if hasattr(args, 'image') and not isinstance(args.image, str):
        raise TypeError(
            'Expected type str passed to -i or --image but received '\
            f'{type(args.video).__name__}. See -h for more information.')
    if hasattr(args, 'sep') and not isinstance(args.sep, str):
        raise TypeError(
            'Expected type str passed to -s or --sep but received '\
            f'{type(args.sep).__name__}. See -h for more information.')
    if hasattr(args, 'window') and not isinstance(args.window, int):
        raise TypeError(
            'Expected type int passed to -w or --window but received '\
            f'{type(args.window).__name__}. See -h for more information.')
    if hasattr(args, 'print') and not isinstance(args.print, bool):
        raise TypeError(
            'Expected type bool passed to -p or --print but received '\
            f'{type(args.print).__name__}. See -h for more information.')

    # Determine whether the script was run stand-alone or from its container
    # based on whether the file argument contained a full directory chain.
    # If stand-alone, also make sure a video directory was provided.
    # Otherwise, there is no way of knowing where to find them.
    if len(os.path.dirname(args.file)) > 0:
        container = False
        dbFile = args.file
        if not hasattr(args, 'video'):
            raise ValueError(
                'Passing a full directory chain to "-f" or "--file" '\
                'indicates this program is being run stand-alone instead '\
                'of within its container. This requires that the video '\
                'directory be passed to "-v" or "--video", but none was '\
                'detected. See -h for more information.')
        if not hasattr(args, 'image'):
            raise Warning(
                'No image directory was passed to "-i" or "--image". '\
                'Images will be written to the present working directory by '\
                'default.')
    else:
        container = True
        dbFile = os.path.join('/data', args.file)
    
    # Store video and image directories if running in container
    if container:
        args.video = '/videos'
        args.image = '/images'

    # Read in database file. Try to determine the delimiter from the file
    # extension if not passed as a command line argument. If this fails, user
    # is prompted to specify and try again.
    if not hasattr(args, 'sep'):
        if args.file[-3:] == 'tsv':
            args.sep = '\t'
        elif args.file[-3:] == 'csv':
            args.sep = ','
        else:
            args.sep = None
    try:
        df = pd.read_csv(dbFile, delimiter=args.sep,
                         usecols=['ImagePtPair', 'FilenameLeft', 'FrameLeft',
                                  'FilenameRight', 'FrameRight', 'Length',
                                  'Family', 'Genus', 'Species', 'Number'],
                        engine='python')
    except ValueError:
        raise ValueError(
            f'Unable to parse the file "{args.file}" using separator '\
            f'"{args.sep}". Relaunch with the proper separator passed '\
            'to -s or --sep flag (e.g., " " for one space, ";" for '\
            'semicolon, etc., without quotations.')
    
    # Fill in missing annotation information
    df['Family'].fillna('fam', inplace=True)
    df['Genus'].fillna('gen', inplace=True)
    df['Species'].fillna('sp', inplace=True)

    # Extract frames from each channel
    channels = ['left', 'right']
    for channel in channels:
        getFrames(data=df, args=args, channel=channel)
    print('Done!')

if __name__ == '__main__':
    """Main program"""
    main()