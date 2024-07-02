import os
import pytube
from moviepy.editor import *

# Define the youtube video URL.
youtube_url = "https://www.youtube.com/watch?v=E6eKvji_BoE"

# Create a Pytube object and get the audio stream
yt = pytube.YouTube(youtube_url)
audio_stream = yt.streams.filter(only_audio=True).first()

# Download the audio as a temporary file
temp_file = audio_stream.download()

# Convert the audio stream to an MP3 file using MoviePy
audio_clip = AudioFileClip(temp_file)
mp3_file = os.path.join("Give your own path", "Name.mp3")
audio_clip.write_audiofile(mp3_file)

# Clean up the temporar file.
os.remove(temp_file)

print("Audio extracted and saved as MP3 file to", mp3_file)