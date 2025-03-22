from datetime import datetime, timedelta
from os import listdir

path = "C:/Users/damum/Downloads/srt/now"
fileList = listdir(path)
outputFile = open("E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/Tamil/Output SRT Analysis.txt","w")
reportFile = open("E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/Tamil/Zones Out of Range.txt","w")

audioMetadata = {}
actualAudioDurations = open("E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/Tamil/Audio Length.txt","r")
audioData = actualAudioDurations.readlines()
actualAudioDurations.close()
for line in audioData:
    audioLength, audioName = line.partition("\t")[::2]
    audioMetadata[audioName.replace("\n","")[:-4]] = audioLength[:7]

reportFile.writelines(f"Filename\tStart\tEnd\tLength\tZone Number\n")
totalUsable = timedelta()
zonesTotal = 0
for file in fileList:
    fileName = f"{path}/{file}"
    txtFile = open(fileName,"r")
    content = txtFile.readlines()
    txtFile.close()
    file = file.replace("(1)","").replace("(2)","").replace(".SRT","").replace(" ","").replace("(3)","")
    actualDuration = audioMetadata[file[:-4]]
    zonesOutOfRange = []
    allVal = []
    secondsTotal = 0
    zones = 0
    usableDuration = timedelta()
    for i in range(1,(len(content)),4):
        zonesTotal = zonesTotal + 1
        zones = zones + 1
        startTime = datetime.strptime(content[i][0:8], '%H:%M:%S')
        endTime = datetime.strptime(content[i][-13:-5], '%H:%M:%S')
        val = (endTime-startTime).seconds
        usableDuration = usableDuration + (endTime-startTime)
        allVal.append(val)
        secondsTotal = secondsTotal + val
        if(file[-6]=="_"):
            reportFile.writelines(f"{file[:-11]}\n")
        else:
            reportFile.writelines(f"{file[:-9]}\n")
        if(val > 13 or val < 7):
            zonesOutOfRange.append(f"{val} {content[i-1][:-1]} {file}")
            # if(file[-6]=="_"):
            #     reportFile.writelines(f"{file[:-11]}\t{startTime.hour}:{startTime.minute}:{startTime.second}\t{endTime.hour}:{endTime.minute}:{endTime.second}\t{val}\t{content[i-1][:-1]}\n")
            # else:
            #     reportFile.writelines(f"{file[:-9]}\t{startTime.hour}:{startTime.minute}:{startTime.second}\t{endTime.hour}:{endTime.minute}:{endTime.second}\t{val}\t{content[i-1][:-1]}\n")
            
    outputFile.writelines(f"{actualDuration}\t{usableDuration}\t{max(allVal)}\t{min(allVal)}\t{file}\t{zones}\n")
    totalUsable = totalUsable + timedelta(seconds=secondsTotal)
outputFile.close()
reportFile.close()
print(totalUsable)
print(zonesTotal)
# print(int(len(content)/4))
# print(usableDuration)
# print(allVal)
# print(secondsTotal)
# print(max(allVal))
# print(fileList)
