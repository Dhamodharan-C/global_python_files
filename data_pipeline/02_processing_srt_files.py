from datetime import datetime, timedelta
from os import listdir

path = "/home/damu/Downloads/srt/hi_0001_rahulgandhi/"

totalUsable = timedelta()
totalDuration = timedelta()

fileList = listdir(path)
for file in fileList:
    fileName = path + file
    txtFile = open(fileName,"r")
    content = txtFile.readlines()
    txtFile.close()
    file = file.replace("(1)","").replace("(2)","").replace(".SRT","").replace(" ","").replace("(3)","")
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
    print(f"{file}\t{usableDuration}\t{len(allVal)}\t{max(allVal)}\t{min(allVal)}")
    totalUsable = totalUsable + timedelta(seconds=secondsTotal)

print(f"Total usable hours : {totalUsable}")