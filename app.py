import yt_dlp
import os
from datetime import datetime

def download_youtube_as_mp3():
    # Ask the user for the YouTube video link
    youtube_url = input("Enter the YouTube video URL: ")

    # Get the current directory
    current_directory = os.getcwd()

    # Generate a timestamp for the filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    temp_file_name = f"temp_audio_{timestamp}.%(ext)s"
    final_file_name = f"audio_{timestamp}.mp3"

    # Step 1: Download the YouTube video
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(current_directory, temp_file_name),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    
    # Rename the file to the timestamped name
    temp_audio_file = os.path.join(current_directory, f"temp_audio_{timestamp}.mp3")
    new_audio_file = os.path.join(current_directory, final_file_name)
    os.rename(temp_audio_file, new_audio_file)

    print(f"Downloaded and converted: {new_audio_file}")

# Call the function
download_youtube_as_mp3()