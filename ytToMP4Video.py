# importing packages
from pytube import YouTube
import os

# Determine the user's default download folder based on the operating system
if os.name == 'posix':  # Unix/Linux/Mac
    default_download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
elif os.name == 'nt':   # Windows
    default_download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
else:
    raise Exception("Unsupported operating system")

# url input from user
yt = YouTube(input("Enter the URL of the video you want to download: \n>> "))

# Choose the video stream with desired quality (for example, '720p')
video_stream = yt.streams.filter(file_extension='mp4', resolution='720p').first()

# download the video file
out_file = video_stream.download(default_download_folder)

print(f"Video downloaded and saved as: {out_file}")
