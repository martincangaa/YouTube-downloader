# YouTube-downloader
A YouTube video or audio downloader based on pytube.

``` python
import pkg_resources
import subprocess

directory = ""          # Paste here the directory in which you want to download the file Ex: C:/Users/user/Desktop (pd: Remember to use / intead of \ windows default)
library = "pytube"

# Check if the library 'pytube' is installed, if it is not, the script installs it and then keeps running
try:
    pkg_resources.get_distribution(library)
    print(f"{library} it is installed")

except pkg_resources.DistributionNotFound:
    print(f"{library} it is not installed. Installing {library}...")
    subprocess.check_call(["pip", "install", library])
    print(f"{library} it has been installed yuhuu!!")

from pytube import YouTube

print("What do you want to do [1] download video / [2] download only the audio:")

start  = int(input()) 
url = str(input("Paste the link of the video: "))

def getStart():
    if(start == 1 or start == 2):
        return start
    else:
        print("You have not introduced a valid value.")

def download_video():
    if(getStart() == 1):  
        yt = YouTube(url).streams.get_highest_resolution()
        try:
            yt.download(directory)
        except:
            print("Error downloading the video.")
    else:
        yt = YouTube(url).streams.get_audio_only()
        try:
            yt.download(directory)
        except:
            print("Error downloading the audio.")
    
download_video()
```
