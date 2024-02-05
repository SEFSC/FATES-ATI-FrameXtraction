---
title: frameXtract Documentation
summary: Instructions for using the application
tags: [getting_started, about, overview]
toc: false
editme: false
search: exclude
---

# Installation

There are two ways of using this script, each with its own dependencies, installation, and usage instructions:

### Method 1: Docker container from GitHub (preferred)

The preferred method of usage is to run the script within its [Docker container](https://www.docker.com/){:target="_blank" rel="noopener"}, which includes the following components:
1. **frameXtract.py**: Python script
2. **requirements.txt**: Python library dependencies
3. **Dockerfile** and **docker-compose.yml**: Docker container configuration files

#### Dependencies

This method requires a local installation of:
1. [Docker](https://www.docker.com/){:target="_blank" rel="noopener"} or [Docker Desktop](https://www.docker.com/products/docker-desktop/){:target="_blank" rel="noopener"} (recommended)
2. [GitHub Desktop](https://desktop.github.com/){:target="_blank" rel="noopener"} or [GitHub Command Line Interface (CLI)](https://cli.github.com/){:target="_blank" rel="noopener"}

Python package dependencies are not listed here because they are installed automatically within the Docker container, so the user need not worry about them.

#### Setup

1. Install the dependencies listed above.
2. [Clone the GitHub repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository){:target="_blank" rel="noopener"} **or** download the Docker container files listed above from the repository, either separately or as a .zip package, ensuring that they are all end up co-located in the same local directory.
   
   By default, the Python script, the data spreadsheet, and video files are all expected to be in the same directory, and the images will also be written to this same directory. In this case, either download the container files listed above into the same directory as the data and video files, or download the container files into a new directory and then copy or move the data and video files into that directory.
   
3. If the data spreadsheet file and video files are in separate directories, and/or if the images are to be written elsewhere, the ```docker-compose.yml``` file needs to be modified as follows:
      * *Data file*: Under the ```volumes``` heading, replace the "." before the colon (:) for the data directory with the full local directory of the data file. For example, if the data file is on a local Windows desktop, the new entry should read:
      
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

    {% include warning.html content="DO NOT change the directory chains *after* the colons. Doing so will break the script." %}

    {{site.data.alerts.note}}
    <ol type="1">
    <li>Docker is platform-agnostic. Mac OS or Linux directory chains can be used here as well.</li>
    <li>One can set any or all of the images, videos, or data directories. Any combination will work. The leading period (.) means "here" and is used to specify the current directory. Thus, if either the videos or the database annotations file are located in the same directory as the program, the volume mapping should retain the default ".".</li>
    <li>This section of ```docker-compose.yml``` maps local directories to independent directories inside the container. The container will only be able to see the contents of local directories mounted here. If you run into "file not found" errors, look here first.</li>
    </ol>
    {{site.data.alerts.end}}

 4. Open a Command Prompt (Windows) or Terminal (Mac) and navigate to the directory containing the container files.
 5. Launch Docker or Docker Desktop, which must be running in order for the next commands to work.
 6. Build the Docker container:

    ```shell
    docker-compose build
    ```


#### Usage

To execute, run

```shell
docker-compose run framextract -f dataFilename.ext
```

where ```dataFilename.ext``` is the name of the annotations database file. (Do not pass the full directory chain; just the file name.) Additional options are described below.


### Method 2: Stand-alone Python script

#### Dependencies

**Warning:** This method may be finicky due to potential version conflicts if the virtual environment (VE) does not get set up properly. Proceed at your own risk.

This method requires local installations of:
1. Optional [Anaconda](https://www.anaconda.com/){:target="_blank" rel="noopener"} for Python and VE management
2. [Python](https://www.python.org/downloads/){:target="_blank" rel="noopener"}. frameXtract was written using Python 3.11.
3. [GitHub Desktop](https://desktop.github.com/){:target="_blank" rel="noopener"} or [GitHub Command Line Interface (CLI)](https://cli.github.com/){:target="_blank" rel="noopener"}
4. Python package dependencies listed in the accompanying [requirements.txt](https://github.com/MattGrossi-NOAA/SEFSC-FATES-ATI-FrameXtraction/blob/main/requirements.txt){:target="_blank" rel="noopener"} file. Currently, only two libraries are needed:
    - [Pandas v2.1.0](https://pandas.pydata.org/docs/whatsnew/v2.1.0.html){:target="_blank" rel="noopener"}
    - [opencv-python-headless](https://pypi.org/project/opencv-python-headless/){:target="_blank" rel="noopener"}

#### Setup

1. Install the GitHub clients above.
2. Install Anaconda (optional; includes Python) or Python.
3. [Clone this GitHub repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository){:target="_blank" rel="noopener"}. Alternatively, download the script file ```frameXtract.py``` and the package dpendency file ```requirements.txt``` from the repository.
4. **Highly recommended:** [Create a virtual environment](https://docs.python.org/3/library/venv.html){:target="_blank" rel="noopener"} and install the package dependencies in ```requirements.txt```.

#### Usage

Execute by passing a *full directory path* for the data spreadsheet file using ```-f``` or ```--file``` **and** a full directory path for the videos to ```-v``` or ```--video``` **and** (optionally) a full directory path for new images to ```-i``` or ```--image```. Full directories will tell the script that it is being run stand-alone instead of within a container:

   ```shell
   python framextract.py --file full/path/to/dataFilename.ext --video full/path/to/videoFiles --image full/path/for/imageFiles
   ```

<p style="text-align:right; font-size:large;">
    <a href="{{ site.url }}{{ site.baseurl }}/about.html"> <b>Usage</b> &#9654; </a>
</p>