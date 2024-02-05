---
title: frameXtract Documentation
summary: Instructions for using the application
tags: [getting_started, about, overview]
toc: false
editme: false
search: exclude
---

# Usage

**frameXtract** is entirely command-line. The syntax for execution differs slightly depending on how the user opts to download, install, and use the script. See [Installation]({{ site.url }}{{ site.baseurl }}/howto.html){:target="_blank" rel="noopener"} instructions for more information.

To summarize:

If installed using [Method 1]({{ site.url }}{{ site.baseurl }}/howto.html#method-1-docker-container-from-github-preferred){:target="_blank" rel="noopener"}, execute with

```shell
docker-compose run framextract -f dataFilename.ext
```

where ```dataFilename.ext``` is the name of the annotations database file. (Do not pass the full directory chain; just the file name.)

If installed using [Method 2]({{ site.url }}{{ site.baseurl }}/howto.html#method-2-stand-alone-python-script){:target="_blank" rel="noopener"}, execute by passing a *full directory path* for the data spreadsheet file using ```-f``` or ```--file``` **and** a full directory path for the videos to ```-v``` or ```--video``` **and** (optionally) a full directory path for new images to ```-i``` or ```--image```. Full directories will tell the script that it is being run stand-alone instead of within a container:

```shell
python framextract.py --file full/path/to/dataFilename.ext --video full/path/to/videoFiles --image full/path/for/imageFiles
```

Additional options are described below.

## Options

This program contains a number of options to customize usage, a summary of which can be accessed by using the ```-h``` or ```--help``` flag, for example:

```shell
docker-compose run framextract -h
```
[](#f-file-data-spreadsheet-file-name)
### f, file: data spreadsheet file name

**-f, -\-file**

This is the only required argument when using the preferred [Method 1]({{ site.url }}{{ site.baseurl }}/howto.html#method-1-docker-container-from-github-preferred){:target="_blank" rel="noopener"}. It specifies the data spreadsheet file to consult for extracting frames. The spreadsheet must contain the following columns of information:
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

### s, sep: separator

**-s, -\-sep**

This specifies the separator (delimiter) for the data spreadsheet file. If no separator is provided at execution, the script tries to determine the separator from the file extention (e.g., "tsv" indicates tab-delimited, "csv" indicates comma-separated) or let the Python parsing engine try to automatically determine it. If these attempts fail, the program will exit and the user will be prompted to re-launch using this flag. This flag is generally not needed in most cases if the file is tab or comma separated, as the automatic determination should rarely fail in either of these cases.

Example:

```shell
docker-compose run framextract --file dataFilename.ext --sep \t 
```

### w, window: window for frame extraction

**-w, -\-window**

For some applications, it may be appropriate to extract a range of frames rather than a single frame. This flag allows the user to specify a number of frames before and after the frame number reported in the spreadsheet to extract. For example, if this is set to 5 and the data contains an annotation at frame 45, then frames 40-50 will be extracted and saved separately (45 $\pm$ 5). For a video recorded at 10 frames per second, this corresponds to one second worth of frames.

Example:

```shell
docker-compose run framextract --file dataFilename.ext --window 5
```

### v, video: video directory

**-v, -\-video**

This provides the user the ability to specify where the videos are located. **It is only used if, and required when, the program is run stand-alone outside of its Docker container, which is not recommended.** This is never needed if the program is run from its Docker container -- in fact, it will be ignored in this case, since the video location would be provided in the ```docker-compose.yml``` file, as decribed above.

### i, image: image directory

**-i, -\-image**

This provides the user the ability to specify where the images should be saved. **It is only used if the program is run stand-alone outside of its Docker container, which is not recommended.** This is never needed if the program is run from its Docker container -- in fact, it will be ignored in this case, since the image location would be provided in the ```docker-compose.yml``` file, as decribed above.

### p, print: print status dialogues to screen

**-p, -\-print**

This takes no arguments; passing it will print updates of successful file reading and writing to the screen.

Example:

```shell
docker-compose run framextract --file dataFilename.ext --window 5 -p
```

### -h, \-\-help: help string

Displays the help documentation.

*This program remains under active development. This page will be updated as the script evolves.*

<p style="text-align:right; font-size:large;">
    <a href="{{ site.url }}{{ site.baseurl }}/blob/main/frameExtractionFromVideo.ipynb"> <b>Demonstration</b> &#9654; </a>
</p>