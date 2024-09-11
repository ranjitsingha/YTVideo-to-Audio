import yt_dlp
from pydub import AudioSegment
import os

def download_youtube_as_mp3(output_folder="."):
    # Ask the user for the YouTube video link
    youtube_url = input("Enter the YouTube video URL: ")

    # Step 1: Download the YouTube video
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_folder, 'temp_audio.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'postprocessor_hooks': [],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    # Step 2: Rename the file to .mp3
    temp_audio_file = os.path.join(output_folder, 'temp_audio.mp3')
    print(f"Downloaded and converted: {temp_audio_file}")

# Call the function
download_youtube_as_mp3(output_folder="./downloads")
