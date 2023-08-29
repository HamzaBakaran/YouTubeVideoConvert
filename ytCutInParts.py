import os
import subprocess
from pytube import YouTube
from moviepy.editor import VideoFileClip

def download_youtube_video(url, output_path):
    yt = YouTube(url)
    video_stream = yt.streams.get_highest_resolution()
    video_filename = yt.title + '.mp4'
    video_path = os.path.join(output_path, video_filename)
    video_stream.download(output_path, filename=video_filename)
    return video_path

def cut_and_add_text(video_path, output_path, part_num, start_time, end_time):
    output_filename = os.path.join(output_path, f"part{part_num}.mp4")

    command = [
        "ffmpeg", "-ss", str(start_time), "-i", video_path, "-t", str(end_time - start_time),
        "-vf", f"drawtext=text='Part {part_num}':fontsize=50:fontcolor=white:x=(w-text_w)/2:y=h-th-20",
        "-c:v", "libx264", "-c:a", "aac", output_filename
    ]
    
    subprocess.run(command, shell=False)

if __name__ == "__main__":
    youtube_url = input("Enter the URL of the YouTube video: ")
    
    os.makedirs("output_directory", exist_ok=True)
    output_directory = "output_directory"

    part_duration = 180  # Duration of each part in seconds
    video_path = download_youtube_video(youtube_url, output_directory)

    # Use moviepy to calculate total duration
    video_clip = VideoFileClip(video_path)
    total_duration = video_clip.duration

    # Get the name of the video (without file extension)
    video_name = os.path.splitext(os.path.basename(video_path))[0]

    # Create a directory with the name of the video
    video_folder = os.path.join(output_directory, video_name)
    os.makedirs(video_folder, exist_ok=True)

    num_parts = int(total_duration / part_duration) + 1

    for part_num in range(num_parts):
        start_time = part_num * part_duration
        end_time = min((part_num + 1) * part_duration, total_duration)
        cut_and_add_text(video_path, video_folder, part_num + 1, start_time, end_time)
        print(f"Part {part_num + 1} saved.")

    print("Video cut into parts and saved in the output directory.")
