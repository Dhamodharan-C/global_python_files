from datetime import datetime, timedelta
from os import listdir

path = "C:/Users/damum/Downloads/Sri"
# path = path.replace("\\","/")
files = listdir(path)
for file in files:
    # file = "sp_0638_bodysoultamil_1892"
    fileName = f"{path}/{file}"
    txtFile = open(fileName,"r")
    content = txtFile.readlines()
    txtFile.close()
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
        if(val > 12 or val < 5):
            zonesOutOfRange.append(f"{val} {content[i-1][:-1]} {file}")
            # reportFile.writelines(f"{val}\t{content[i-1][:-1]}\t{file}\n")
    print(f"Speaker Name    : {file[:-4]}")
    print(f"Usable Duration : {usableDuration}")
    print(f"Maximum Length  : {max(allVal)}")
    print(f"Minimum Length  : {min(allVal)}")
