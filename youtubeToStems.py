
from __future__ import unicode_literals
import youtube_dl
import os
import subprocess
from datetime import date

today = date.today()
date = today.strftime("%d-%m-%Y")
folder = "audio_output_" + date


spleeter = "spleeter separate -c mp3 -o " + folder + " -p spleeter:5stems "

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}
 
inputFile = open('inputFile.txt', 'r')
count = 0
 
print("\n\n---SONG DOWNLOAD ---\n")

while True:
    link = inputFile.readline() # Get next link from file
    if not link: # if line is empty or end of file is reached
        break

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
        print(" ")
    count += 1
 
print(f"\nTotal files downloaded: {count}")
 
inputFile.close()

print("\n\n---TRACK SEPARATION ---\n")

entries = os.listdir('./')
for file in entries:
    newFile = file.replace("(","[").replace(")","]")#.replace(" ","")
    os.rename(file, newFile)
    if ".mp3" in newFile:
        print(f"\nSeparating: {newFile}")
        # print(spleeter + newFile)
        subprocess.call(spleeter + " \"" + newFile + "\"" , shell=True)
        os.remove(newFile)


print(f"\nAll files separated. Stems can be found in {folder}")

