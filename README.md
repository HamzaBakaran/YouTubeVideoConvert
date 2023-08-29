# YouTubeVideoConvert

# YouTube Video Cutter and Downloader

This repository contains Python scripts to download YouTube videos and cut them into parts while adding text annotations. It utilizes the `pytube` and `moviepy` libraries for these tasks.

## Instructions

### Video Cutter and Text Annotation Script (`ytCutInParts.py`)

 Install the required packages using the following command:
```sh
pip install pytube moviepy
```
## Run the Script:

Run the script:

```sh
python ytCutInParts.py
```
### Provide YouTube URL

Enter the URL of the YouTube video when prompted.

### Video Cutting and Annotation

The script will download the video and cut it into parts of a specified duration, adding text annotations to each part.

## Video Downloader Script (`ytToMP4Video.py`)

This script allows you to download a video from a URL using the `pytube` library.

### Install Dependencies

Install the required package using the following command:

```sh
pip install pytube
```

## Run the Script

Run the script:

```sh
python ytToMP4Video.py
```
Follow the prompts to enter the URL of the video you want to download.  

### Video Downloading
The script will determine your default download folder based on your operating system and download the video there.




