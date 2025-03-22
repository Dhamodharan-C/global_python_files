from os import listdir
# from mutagen.mp3 import MP3
from librosa import get_duration
from datetime import timedelta, time

path = "/home/damu/ISRL/English_MS/split_files/"
# path = "/media/damu/Office/India_Speaks/mann_ki_baat/audio_files/"
audioFiles = listdir(path)
outputFile = "/home/damu/ISRL/English_MS/audio_length.txt"
out = open(outputFile,"w")
totalDuration = timedelta()
for file in audioFiles:
    # if len(file[:-11]) < 7 :
    # totalDuration = timedelta(seconds = MP3(f"{path}{file}").info.length)
    totalDuration = get_duration(path = f"{path}{file}")
    totalDuration = timedelta(seconds=totalDuration)
    out.writelines(f"{totalDuration}\t{file}\n")
out.close()
