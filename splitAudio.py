from pydub import AudioSegment
from os import listdir
import datetime

# ---Path Allocation---
importPath = "E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/Tamil/New Audios/"
exportPath = "E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/Tamil/cut_Audio_Files/Sliced Audio Files/"
names = open("E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/Tamil/Cut Files.txt",'r')
files = names.readlines()
names.close()
# ---dependencies---
AudioSegment.converter = "ffmpeg.exe"
AudioSegment.ffmpeg = "ffmpeg.exe"
AudioSegment.ffprobe = "ffprobe.exe"
# ---Assigning Audio File---
stt = datetime.datetime.now()
for file in files:
    st = datetime.datetime.now()
    fileName = file.replace("\n","")
    audio = AudioSegment.from_mp3(importPath + fileName)
    # Clip size in minutes
    clipSize = 20
    minClipSize = 5
    # ---Conversion to milliseconds---
    msClipSize = clipSize*60*1000
    msMinClipSize = minClipSize*60*1000
    # ---Variables---
    audioLength = len(audio)
    numberOfClips = audioLength // msClipSize
    lastClipSize = audioLength % msClipSize
    for clipCounter in range(1,(numberOfClips + 2)):
        if(audioLength > msMinClipSize):
            if(audioLength == lastClipSize):
                starting = ((clipCounter-1)*msClipSize)
                ending = len(audio)
            else:
                starting = ((clipCounter-1)*msClipSize)
                ending = (clipCounter*msClipSize)
            extract = audio[starting : ending]
            extract.export(f"{exportPath + fileName[0:-4]}_{clipCounter}.mp3", format = "mp3")
            audioLength = audioLength - msClipSize
    print(f"{datetime.datetime.now()-st}\t{file}")
print(datetime.datetime.now()-stt)
