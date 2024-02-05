---
title: frameXtract Documentation
summary: Instructions for using the application
tags: [getting_started, about, overview]
toc: false
editme: false
search: exclude
---

# frameXtract

**frameXtract** is a simple tool for extracting frames from stereo videos and saving them as images. Its usage is demonstrated in a [Jupyter notebook](https://github.com/MattGrossi-NOAA/SEFSC-FATES-ATI-FrameXtraction/blob/main/frameExtractionFromVideo.ipynb){:target="_blank" rel="noopener"} for informational purposes.

# Overview

**frameXtract** reads a data spreadsheet exported from fish measurement software and extracts the frame number corresponding to each annotation in each stereo video. The database is expected to contain the following columns of information:
- *FilenameLeft* - name of video files corresponding to left stereo channel
- *FilenameRight* - name of video files corresponding to right stereo channel
- *FrameLeft* - frame numbers to be extracted from *FilenameLeft*
- *FrameRight* - frame numbers to be extracted from *FilenameRight*
- *Length* - length of fish appearing in (*FrameLeft*, *FrameRight*) frame pair
- *Family* - taxonomic family classification of fish appearing in (*FrameLeft*, *FrameRight*) frame pair. If missing, will be filled with "fam".
- *Genus* - taxonomic genus classification of fish appearing in (*FrameLeft*, *FrameRight*) frame pair. If missing, will be filled with "gen".
- *Species* - taxonomic species classification of fish appearing in (*FrameLeft*, *FrameRight*) frame pair. If missing, will be filled with "sp".

Optionally, a window can be passed to extract a specified number of frames on each side of the specified frame number. Images are written as jpg files following the naming convention:

```shell
videoFileName_frame-N_length-L.jpg
```

where N is the zero-padded frame number extracted from video file ```videoFileName``` and L is the length of the fish in the image. New image files are saved in species-specific subdirectories ```./family/genus/species/```, which are automatically created if they do not already exist. See below for instructions on how to control where these subdirectories are created.

# Release Notes

<details>
  <summary>
    <b> &#9660; Version History </b>
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


# Disclaimer
This utility is a scientific product and is not official communication of the National Oceanic and Atmospheric Administration, or the United States Department of Commerce. All NOAA GitHub project code is provided on an "as is" basis and the user assumes responsibility for its use. Any claims against the Department of Commerce or Department of Commerce bureaus stemming from the use of this GitHub project will be governed by all applicable Federal law. Any reference to specific commercial products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply their endorsement, recommendation or favoring by the Department of Commerce. The Department of Commerce seal and logo, or the seal and logo of a DOC bureau, shall not be used in any manner to imply endorsement of any commercial product or activity by DOC or the United States Government.

<p style="text-align:right; font-size:large">
    <a href="{{ site.url }}{{ site.baseurl }}/howto.html"> <b>Installation</b> &#9654; </a>
</p>