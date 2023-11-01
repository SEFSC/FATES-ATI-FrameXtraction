# imageXtraction
 Simple tool for extracting frames from stereo videos and saving as images as described in [frameExtractionFromVideo.ipynb](https://github.com/MattGrossi-NOAA/SEFSC-FATES-ATI-FrameXtraction/blob/main/frameExtractionFromVideo.ipynb).

<details>
  <summary>
    <b> Version History </b>
  </summary>
  <ul>
    <li> <b>Version 1.0</b> (Sep 2023): Initial version </li>
    <li> <b>Version 1.1</b> (Oct 2023): Revised to include:
      <ul>
        <li> Appending fish length to image file name </li>
        <li> Ability to control where images are read from and saved </li> 
        <li> Storing images in species-specific subdirectories </li>
      </ul> </li>
  </ul>
</details>

<details>
  <summary>
    <b> Feature Requests </b>
  </summary>
  <ul>
    <li> None </li>
  </ul>
</details>

## Overview
This script reads a data spreadsheet exported from fish measurement software and extracts the frame number corresponding to each annotation in each stereo video. The database is expected to contain the following columns of information:
- *FilenameLeft* - name of video files corresponding to left stereo channel
- *FilenameRight* - name of video files corresponding to right stereo channel
- *FrameLeft* - frame numbers to be extracted from *FilenameLeft*
- *FrameRight* - frame numbers to be extracted from *FilenameRight*
- *Length* - length of fish appearing in (*FrameLeft*, *FrameRight*) frame pair
- *Family* - taxonomic family classification of fish appearing in (*FrameLeft*, *FrameRight*) frame pair. If missing, will be filled with "fam".
- *Genus* - taxonomic genus classification of fish appearing in (*FrameLeft*, *FrameRight*) frame pair. If missing, will be filled with "gen".
- *Species* - taxonomic species classification of fish appearing in (*FrameLeft*, *FrameRight*) frame pair. If missing, will be filled with "sp".

Optionally, a window can be passed to extract a specified number of frames on each side of the specified frame number -- see below for details. Images are written as jpg files following the naming convention:

```shell
videoFileName_frame-N_length-L.jpg
```

where N is the zero-padded frame number extracted from video file ```videoFileName``` and L is the length of the fish in the image. New image files are saved in species-specific subdirectories ```./family/genus/species/```, which are automatically created if they do not already exist. See below for instructions on how to control where these subdirectories are created.

## Usage

The preferred method of usage is to run the script within its [Docker container](https://www.docker.com/). You will need to [install Docker](https://www.docker.com/) or [Docker Desktop](https://www.docker.com/products/docker-desktop/) (recommended) locally for this to work. The container includes the following components:
1. **frameXtract.py**: Python script
2. **requirements.txt**: Python library dependencies
3. **Dockerfile** and **docker-compose.yml**: Docker container configuration files

### Method 1: Docker container from GitHub (preferred)
1. Install [GitHub Desktop](https://desktop.github.com/) or [GitHub Command Line Interface (CLI)](https://cli.github.com/).
2. [Clone this GitHub repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository). Alternatively, download the files listed above from the repository, either separately or as a .zip package, ensuring that they are all end up co-located in the same local directory.
   
    a. By default, the Python script, the data spreadsheet, and video files are all expected to be in the same directory, and the images will also be written to this same directory. In this case, either download the container files listed above into the same directory as the data and video files, or download the container files into a new directory and then copy or move the data and video files into that directory.
   
    b. If the data spreadsheet file and video files are in separate directories, and/or if the images are to be written elsewhere, the ```docker-compose.yml``` file needs to be modified as follows:
      * *Data file*: Under the 'volumes' heading, replace the "." before the colon (:) for the data directory with the full local directory of the data file. For example, if the data file is on a local Windows desktop, the new entry should read:
        ```yml
        volumes:
          # Application directory
          - .:/home
          # Image directory
          - .:/images
          # Video directory
          - .:/videos
          # Data directory
          - C:\Users\user.name\Desktop:/data
        ```
      * *Video files*: Replace the "." before the colon (:) for the video directory with the full local directory containing the video files. For example, if the video files are on another drive, the new entry might read:
        ```yml
        volumes:
          # Application directory
          - .:/home
          # Image directory
          - .:/images
          # Video directory
          - D:\myVideos:/videos
          # Data directory
          - C:\Users\user.name\Desktop:/data
        ```
      * *Image files*: To change where the images are written locally, replace the "." before the colon (:) for the image directory with the full local directory where the new image files, sorted by fish species, should be written. For example, if the image files are to be written in the local Documents folder, the new entry should read:
        ```yml
        volumes:
          # Application directory
          - .:/home
          # Image directory
          - C:\Users\user.name\Documents\images:/images
          # Video directory
          - D:\myVideos:/videos
          # Data directory
          - C:\Users\user.name\Desktop:/data
        ```
      * *Application file (rare)*: In the unlikely event that the Python script is not co-located with the container files, replace the "." before the colon (:) for the application directory with the full local directory containing the script. This should rarely, if ever, be necessary.

    Some things to note:
    1. Docker is platform-agnostic. Mac OS or Linux directory chains can be used here as well.
    2. One can set any or all of the images, videos, or data directories. Any combination will work. The leading period (.) means "here" and is used to specify the current directory. Thus, if either the videos or the database annotations file are located in the same directory as the program, the volume mapping should retain the default ".".
    2. DO NOT change the directory chains *after* the colons. Doing so will break the script.
    4. This section of ```docker-compose.yml``` maps local directories to independent directories inside the container. The container will only be able to see the contents of local directories mounted here. If you run into "file not found" errors, look here first.
  
 3. Open a Command Prompt (Windows) or Terminal (Mac) and navigate to the directory containing the container files.
 5. Launch Docker or Docker Desktop, which must be running in order for the next commands to work.
 5. Build the Docker container:
    ```shell
    docker-compose build
    ```
 6. To execute, run
    ```shell
    docker-compose run framextract -f dataFilename.ext
    ```
    where ```dataFilename.ext``` is the name of the annotations database file. (Do not pass the full directory chain; just the file name.) Additional options are described below.

### Method 2: As a stand-alone Python script
1. [Clone this GitHub repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository). Alternatively, download the script file ```frameXtract.py``` and the package dpendency file ```requirements.txt``` from the repository.
2. Download and install [Python](https://www.python.org/downloads/) if needed. This program was written in Python 3.11.
3. **Highly recommended:** [Create a virtual environment](https://docs.python.org/3/library/venv.html) and install the package dependencies in ```requirements.txt```.
4. Execute by passing a *full directory path* for the data spreadsheet file using ```-f``` or ```--file``` **and** a full directory path for the videos to ```-v``` or ```--video``` **and** (optionally) a full directory path for new images to ```-i``` or ```--image```. This will tell the script that it is being run stand-alone instead of within a container:
   ```shell
   python framextract.py --file full/path/to/dataFilename.ext --video full/path/to/videoFiles --image full/path/for/imageFiles
   ```
   Note that this method may be finicky due to potential version conflicts if the virtual environment does not get set up properly.

## Options

This program contains a number of options to customize usage, a summary of which can be accessed by using the ```-h``` or ```--help``` flag, for example:
```shell
docker-compose run framextract -h
```

### -f, --file: data spreadsheet file name
This is the only required argument when using Method 1 above (preferred). It specifies the data shreadsheet file to consult for extracting frames. It must contain the following columns of information:
- *FilenameLeft* - name of video files corresponding to left stereo channel
- *FilenameRight* - name of video files corresponding to right stereo channel
- *FrameLeft* - frame numbers to be extracted from *FilenameLeft*
- *FrameRight* - frame numbers to be extracted from *FilenameRight*
- *Length* - length of fish appearing in (*FrameLeft*, *FrameRight*) frame pair
- *Family* - taxonomic family classification of fish appearing in (*FrameLeft*, *FrameRight*) frame pair. If missing, will be filled with "fam".
- *Genus* - taxonomic genus classification of fish appearing in (*FrameLeft*, *FrameRight*) frame pair. If missing, will be filled with "gen".
- *Species* - taxonomic species classification of fish appearing in (*FrameLeft*, *FrameRight*) frame pair. If missing, will be filled with "sp".

Example:
```shell
docker-compose run framextract -f dataFilename.ext
```

### -s, --sep: separator
This specifies the separator (delimiter) for the data spreadsheet file. If no separator is provided at execution, the script tries to determine the separator from the file extention (e.g., "tsv"==tab-delimited, "csv"==comma-separated) or let the Python parsing engine try to automatically determine it. If these attempts fail, the program will exit and the user will be prompted to re-launch using this flag. This flag is generally not needed in most cases if the file is tab or comma separated, as the automatic determination should rarely fail in either of these cases.

Example:
```shell
docker-compose run framextract --file dataFilename.ext --sep \t 
```

### -w, --window: window for frame extraction
For some applications, it may be appropriate to extract a range of frames rather than a single frame. This flag allows the user to specify a number of frames before and after the frame number reported in the spreadsheet to extract. For example, if this is set to 5 and the data contains an annotation at frame 45, then frames 40-50 will be extracted and saved separately (45 $\pm$ 5). For a video recorded at 10 frames per second, this corresponds to one second worth of frames.

Example:
```shell
docker-compose run framextract --file dataFilename.ext --window 5
```

### -v, --video: video directory
This provides the user the ability to specify where the videos are located. **It is only used if, and required when, the program is run stand-alone outside of its Docker container, which is not recommended.** This is never needed if the program is run from its Docker container -- in fact, it will be ignored in this case, since the video location would be provided in the ```docker-compose.yml``` file, as decribed above.

### -i, --image: image directory
This provides the user the ability to specify where the images should be saved. **It is only used if the program is run stand-alone outside of its Docker container, which is not recommended.** This is never needed if the program is run from its Docker container -- in fact, it will be ignored in this case, since the image location would be provided in the ```docker-compose.yml``` file, as decribed above.

### -p, --print: print status dialogues to screen
This takes no arguments; passing it will print updates of successful file reading and writing to the screen.

Example:
```shell
docker-compose run framextract --file dataFilename.ext --window 5 -p
```

### -h, --help: help string
Displays the help documentation.

*This program remains under active development. This page will be updated as the script evolves.*

## Workflow

 A demonstration and explanation of the script workflow is provided in an accompanying [Jupyter notebook](https://github.com/MattGrossi-NOAA/SEFSC-FATES-ATI-FrameXtraction/blob/main/frameExtractionFromVideo.ipynb).

# Disclaimer
This repository is a scientific product and is not official communication of the National Oceanic and Atmospheric Administration, or the United States Department of Commerce. All NOAA GitHub project code is provided on an "as is" basis and the user assumes responsibility for its use. Any claims against the Department of Commerce or Department of Commerce bureaus stemming from the use of this GitHub project will be governed by all applicable Federal law. Any reference to specific commercial products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply their endorsement, recommendation or favoring by the Department of Commerce. The Department of Commerce seal and logo, or the seal and logo of a DOC bureau, shall not be used in any manner to imply endorsement of any commercial product or activity by DOC or the United States Government.
