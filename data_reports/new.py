from datetime import datetime, timedelta
from os import listdir
from glob import glob

path = '/home/damu/Downloads/srt/'
outputFile = open("/home/damu/ISRL/Hindi_MS/rahul_gandhi.txt","w")

audioMetadata = {}
actualAudioDurations = open("/home/damu/ISRL/Tamil_MS/tamil_audio_length.txt","r")
audioData = actualAudioDurations.readlines()
actualAudioDurations.close()
for line in audioData:
    audioLength, audioName = line.partition("\t")[::2]
    audioMetadata[audioName.replace("\n","")[:-4]] = audioLength[:7]

subFolders = glob(path + "*", recursive = True)
outputFile.writelines(f"Name\tFile\tActual Duration\tUsable Duration\tZones\tMax\tMin\n")
totalUsable = timedelta()
for folder in subFolders:
    user = folder[(len(path)):]
    fileList = listdir(folder)
    for file in fileList:
        fileName = f"{path}/{user}/{file}"
        txtFile = open(fileName,"r")
        content = txtFile.readlines()
        txtFile.close()
        file = file.replace("(1)","").replace("(2)","").replace(".SRT","").replace(" ","").replace("(3)","")
        actualDuration = audioMetadata[file[:-4]]
        zonesOutOfRange = []
        allVal = []
        secondsTotal = 0
        usableDuration = timedelta()
        for i in range(1,(len(content)),4):
            startTime = datetime.strptime(content[i][0:8], '%H:%M:%S')
            endTime = datetime.strptime(content[i][-13:-5], '%H:%M:%S')
            val = (endTime-startTime).seconds
            usableDuration = usableDuration + (endTime-startTime)
            allVal.append(val)
            secondsTotal = secondsTotal + val
        outputFile.writelines(f"{user}\t{file}\t{actualDuration}\t{usableDuration}\t{len(allVal)}\t{max(allVal)}\t{min(allVal)}\n")
        totalUsable = totalUsable + timedelta(seconds=secondsTotal)
outputFile.close()
print(totalUsable)