import json
from Report import Batch, Recording, getDateAndTime, getDate, oldVersionReport
import datetime
startTime = datetime.datetime.now()
dbFile = '/home/damu/ISRL/Tamil_MS/Reports/Transcription_Database_new.txt'
file1 = open('/home/damu/ISRL/Tamil_MS/Reports/Multiple_Entries_new.txt','w')
file2 = open('/home/damu/ISRL/Tamil_MS/Reports/Null_Entries_new.txt','w')
file3 = open(dbFile, 'r+')
# file4 = open('/home/damu/ISRL/Tamil_MS/add_new/Work_hours_new.txt', 'w')
# file5 = open('/home/damu/ISRL/Tamil_MS/add_new/Yogesh_Report_new.txt', 'w')
# file6 = open('/home/damu/ISRL/Tamil_MS/add_new/Validation_Report_new.txt', 'w')
# file7 = open('/home/damu/ISRL/Tamil_MS/add_new/Multiple_new.txt','w', encoding='utf8')
adminDatas = open('/home/damu/Downloads/tam_ms_new.datas.json','r')
adminUsers = open('/home/damu/Downloads/tam_ms_new.users.json','r')
batches = json.load(adminDatas)
userJson = json.load(adminUsers)
totalUsable = []
total = []
multipleEntries = []
noneCount = []
dates = []
users = []
currentBatch = []
startingDate = datetime.date(2023,8,30)
for obj in range(len(userJson)):
    if userJson[obj]["type"] == "annotator":
        users.append(userJson[obj]["email"])
        currentBatch.append(userJson[obj]["batchAllotted"])
userData = []
checkFiles = []
# file6.writelines(f"Speaker\tFilename\tValidator\tDate\tModified\tTotal Hours\tUsable hours\n")
for batch in range(len(batches)):
    B = Batch(batches[batch]["batchId"],batches[batch]["assignee"],len(batches[batch]["recordings"]),
              batches[batch]["correctedRecordingsCount"],batches[batch]["totalAudioDuration"],batches[batch]["usableAudioDuration"])
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
        # if getDate(R.modified) != "":
            # if B.assignee[-14:] == "@validator.com" and getDate(R.modified) > startingDate:
                # file6.writelines(f"{B.id}\t{R.name}\t{B.assignee}\t{getDate(R.modified)}\t{getDateAndTime(R.modified)}\t{R.totalHours}\t{R.usableHours}\n")
        if R.usableHours != "" and R.usableHours != None and int(R.usableHours-1) <= int(R.totalHours):
            file3.writelines(f"{B.id}\t{B.assignee}\t{B.recordings}\t{B.completed}\t{R.name}\t{R.id}\t{R.totalHours}\t"\
                            f"{R.usableHours}\t{getDateAndTime(R.modified)}\t{status}\t{B.id}-{status}\t{B.id}-{B.assignee}\n")
        else:
            file3.writelines(f"{B.id}\t{B.assignee}\t{B.recordings}\t{B.completed}\t{R.name}\t{R.id}\t{R.totalHours}\t"\
                            f"{0}\t{getDateAndTime(R.modified)}\t{status}\t{B.id}-{status}\t{B.id}-{B.assignee}\n")
        if dates.count(getDate(R.modified)) == 0 and getDate(R.modified) != "": dates.append(getDate(R.modified))
        if R.modified != "": userData.append([B.assignee, getDateAndTime(R.modified), getDate(R.modified), R.totalHours, B.id])
        if(R.usableHours != "" and R.usableHours != None):
            total.append(R.totalHours)
            if(int(R.usableHours-1) > int(R.totalHours)):
                multipleEntries.append(f"{R.name}\t{getDateAndTime(R.modified)}\t{B.assignee}\t"\
                                       f"{round(R.totalHours,2)}\t{round(R.usableHours,2)}\n")
            else:
                totalUsable.append(R.usableHours)
        elif(R.usableHours == None):
            noneCount.append(f"{R.name}\t{getDateAndTime(R.modified)}\t{B.assignee}\t{round(R.totalHours,2)}\n")
            total.append(R.totalHours)
file1.writelines(multipleEntries)
file2.writelines(noneCount)
file1.close()
file2.close()
# file6.close()
file3.close()
yogeshUsers = ["shriharkannan@gmail.com", "arruaravinth3@gmail.com", "jaisarvesh11@gmail.com", "trkvijaybison@gmail.com", 
             "hariaravinth1305@gmail.com", "sowmiya@gmail.com", "sutharsan@gmail.com", "sangaralingam@gmail.com", 
             "sabari@gmail.com", "thaneswar@gmail.com", "sivanezh@gmail.com", "sasikumar@gmail.com", "thulasiram@gmail.com", 
             "krishnakumar@gmail.com", "sangar@gmail.com", "pavithra@gmail.com"]
dates.sort(key = lambda x: datetime.datetime.strptime(str(x), '%Y-%m-%d'))
ref = datetime.timedelta(minutes=15)
# file4.writelines(f"User\tDate\tWorked hours\tUsable hours\n")
# file5.writelines(f"User\tDate\tWorked hours\tUsable hours\n")
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
        # file4.writelines(f"{user}\t{date}\t{round(workMins/3600,2)}\t{round(outMins/3600,2)}\n")
        # if yogeshUsers.count(user) > 0:
            # file5.writelines(f"{user}\t{date}\t{round(workMins/3600,2)}\t{round(outMins/3600,2)}\n")
# file4.close()
# file5.close()

print(f"Total Duration      : {round(sum(total)/3600,2)} Hours")
print(f"Usable Duration     : {round(sum(totalUsable)/3600,2)} Hours")
print(f"Multiple Entries    : {len(multipleEntries)}")
print(f"Null Entries        : {len(noneCount)}")
print(f"Total Entries       : {len(userData)}")
print(f"Total users         : {len(users)}")
print(f"Total days          : {len(dates)}")
print(f"{(datetime.datetime.now() - startTime).seconds} seconds")
