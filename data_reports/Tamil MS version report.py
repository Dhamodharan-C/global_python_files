import json
from Report import Batch, Recording, getDateAndTime, getDate, oldVersionReport
import datetime
startTime = datetime.datetime.now()
dbFile = 'E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/Tamil/Transcription Database.csv'
file1 = open('E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/Tamil/Multiple Entries.txt','w')
file2 = open('E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/Tamil/Null Entries.txt','w')
file3 = open(dbFile, 'r+')
file4 = open('E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/Tamil/Work hours.csv', 'w')
file5 = open('E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/Tamil/Yogesh Report.csv', 'w')
adminDatas = open('C:/Users/damum/Downloads/tamil-tts.datas.json','r')
adminUsers = open('C:/Users/damum/Downloads/tamil-tts.users.json','r')
batches = json.load(adminDatas)
userJson = json.load(adminUsers)
totalUsable = []
total = []
multipleEntries = []
noneCount = []
dates = []
users = []
currentBatch = []
for obj in range(len(userJson)):
    if userJson[obj]["type"] == "annotator":
        users.append(userJson[obj]["email"])
        currentBatch.append(userJson[obj]["batchAllotted"])
userData = []
checkFiles = []
oldReport = oldVersionReport(dbFile)
outputFile = []
hoursMultiple = 0
hoursNone = 0
for batch in range(len(batches)):
    B = Batch(batches[batch]["batchId"],batches[batch]["assignee"],len(batches[batch]["recordings"]),
              batches[batch]["correctedRecordingsCount"],batches[batch]["totalAudioDuration"],batches[batch]["usableAudioDuration"])
    if B.id[-4:] != "_add":
        for recording in range(B.recordings):
            R = Recording(batches[batch]["recordings"][recording]["recordingId"],batches[batch]["recordings"][recording]["recordingName"],
                        batches[batch]["recordings"][recording]["modifiedDate"],batches[batch]["recordings"][recording]["totalDuration"],
                        batches[batch]["recordings"][recording]["usableDuration"])
            if currentBatch.count(B.id) == 0 and B.assignee != "":
                status = "Completed"
            elif currentBatch.count(B.id) == 1 and B.assignee != "":
                status = "Pending"
            else:
                status = "Not assigned"
            if oldReport[R.name][8] == "" and getDateAndTime(R.modified) != "":
                if R.usableHours != "" and R.usableHours != None and int(R.usableHours-1) <= int(R.totalHours):
                    outputFile.append([B.id,B.assignee,str(B.recordings),str(B.completed),R.name,R.id,str(R.totalHours),
                                    str(R.usableHours),str(getDateAndTime(R.modified)),status,B.id + "-" + status,B.id + "-" + B.assignee])
                else:
                    outputFile.append([B.id,B.assignee,str(B.recordings),str(B.completed),R.name,R.id,str(R.totalHours),
                                    str(0),str(getDateAndTime(R.modified)),status,B.id + "-" + status,B.id + "-" + B.assignee])
            else:
                outputFile.append(oldReport[R.name])
            if dates.count(getDate(R.modified)) == 0 and getDate(R.modified) != "": dates.append(getDate(R.modified))
            if R.modified != "": userData.append([B.assignee, getDateAndTime(R.modified), getDate(R.modified), R.totalHours, B.id])
            if(R.usableHours != "" and R.usableHours != None):
                if(int(R.usableHours-1) > int(R.totalHours)):
                    multipleEntries.append(f"{R.name}\t{getDateAndTime(R.modified)}\t{B.assignee}\t"\
                                        f"{round(R.totalHours,2)}\t{round(R.usableHours,2)}\n")
                    hoursMultiple = hoursMultiple + round(R.totalHours,2)
                else:
                    total.append(R.totalHours)
                    totalUsable.append(R.usableHours)
            elif(R.usableHours == None):
                noneCount.append(f"{R.name}\t{getDateAndTime(R.modified)}\t{B.assignee}\t{round(R.totalHours,2)}\n")
                hoursNone = hoursNone + round(R.totalHours,2)
file1.writelines(multipleEntries)
file2.writelines(noneCount)
file1.close()
file2.close()
for entry in outputFile:
    for i in range(len(entry)):
        if i < (len(entry)-1) and i != 0:
            file3.write(f",{entry[i]}")
        elif i == 0:
            file3.write(f"{entry[i]}")
        elif i == (len(entry)-1) and entry[i][:-2] != "\n":
            file3.write(f",{entry[i]}\n")
        else:
            file3.write(f",{entry[i]}")
file3.close()
yogeshUsers = ["shriharkannan@gmail.com", "arruaravinth3@gmail.com", "jaisarvesh11@gmail.com", "trkvijaybison@gmail.com", 
             "hariaravinth1305@gmail.com", "sowmiya@gmail.com", "sutharsan@gmail.com", "sangaralingam@gmail.com", 
             "sabari@gmail.com", "thaneswar@gmail.com", "sivanezh@gmail.com", "sasikumar@gmail.com", "thulasiram@gmail.com", 
             "krishnakumar@gmail.com", "sangar@gmail.com", "pavithra@gmail.com"]
dates.sort(key = lambda x: datetime.datetime.strptime(str(x), '%Y-%m-%d'))
ref = datetime.timedelta(minutes=15)
file4.writelines(f"User,Date,Worked hours,Usable hours\n")
file5.writelines(f"User,Date,Worked hours,Usable hours\n")
for user in users:
    datas = list(filter(lambda d: d[0] == user ,userData))
    datas.sort(key = lambda x: x[1])
    for date in dates:
        workMins = 0
        outMins = 0
        for i in range(1,len(datas)):
            data = datas[i]
            if checkFiles.count(f"{user}/{datas[i][4]}")==0: checkFiles.append(f"{user}/{datas[i][4]}")
            mins = (datas[i][1] - datas[i-1][1])
            if(datas[i][2] == date):
                outMins = outMins + datas[i-1][3]
                if(mins < ref):
                    workMins = workMins + mins.seconds
                else:
                    workMins = workMins + 240
        file4.writelines(f"{user},{date},{round(workMins/3600,2)},{round(outMins/3600,2)}\n")
        if yogeshUsers.count(user) > 0:
            file5.writelines(f"{user},{date},{round(workMins/3600,2)},{round(outMins/3600,2)}\n")
file4.close()
file5.close()
print(f"Total Duration      : {round(sum(total)/3600,2)} Hours")
print(f"Usable Duration     : {round(sum(totalUsable)/3600,2)} Hours")
print(f"Multiple Entries    : {len(multipleEntries)}")
print(f"Multiple Hours      : {round(hoursMultiple/3600,2)}")
print(f"Null Entries        : {len(noneCount)}")
print(f"Null Hours          : {round(hoursNone/3600,2)}")
print(f"Total Entries       : {len(userData)}")
print(f"Total users         : {len(users)}")
print(f"Total days          : {len(dates)}")
print(f"{(datetime.datetime.now() - startTime).seconds} seconds")
# print(checkFiles)
