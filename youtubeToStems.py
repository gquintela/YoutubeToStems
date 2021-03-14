
from __future__ import unicode_literals
import youtube_dl
import os
import subprocess
from datetime import date
import argparse

parser = argparse.ArgumentParser(description='Convert the audio of Youtube videos into stems.')

parser.add_argument('-s', '--stems', dest='stemsQty', nargs='?', default='5', action='store', 
                    help='Quantity of stems:2,4 or 5. default: 5')
parser.add_argument('--input', dest='inputFileName', nargs='?', action='store',
                    default='inputFile.txt',
                    help='Select file to read links (default: inputFile.txt)')

args = parser.parse_args()

today = date.today()
date = today.strftime("%d-%m-%Y")
folder = "audio_output_" + date
stemsQty = args.stemsQty
if(stemsQty != '2' and stemsQty !='4' and stemsQty !='5'):
	print("please select correct ammount of stems: 2, 4 or 5.")
	exit(0)

spleeter = "spleeter separate -c mp3 -o " + folder + " -p spleeter:" + stemsQty + "stems "

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}
 
inputFile = open(args.inputFileName, 'r')
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
if (not count):
	print(f"\n{args.inputFileName} is empty, please fill it with Youtube links or select a new file.")
	exit(0)
 
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

