import json
import datetime, time
from os.path import getmtime
import pathlib
import pandas as pd
import matplotlib.pyplot as plt


filePath = "C:/Users/damum/Downloads/"
nameKey = ["mal_", "hin-", "kannada_"]
validators = []
pruned = []
validatorsDaily = []
for name in nameKey:
    fileName = f"{name}tts.datas.json"
    language = {'mal' : "MALAYALAM",
                'eng' : "ENGLISH",
                'tam' : "TAMIL",
                'hin' : "HINDI",
                'kan' : "KANNADA",
                'tel' : "TELUGU"}
    totalLines = {'mal' : 35000,
                    'eng' : 35000,
                    'tam' : 35000,
                    'hin' : 35000,
                    'kan' : 35000,
                    'tel' : 35000}
    jsonData = open(filePath + fileName,'r', encoding="utf8")
    content = json.load(jsonData)
    asOn = getmtime(filePath + fileName)
    asOn = time.ctime(asOn)
    asOn = datetime.datetime.strptime(str(asOn),"%a %b %d %H:%M:%S %Y")
    tillDate = datetime.datetime.date(asOn)
    # tillDate = datetime.datetime.today()
    asOn = str(asOn)

    def getDateAndTime(timestamp):
        if(timestamp != ""):
            dt = timestamp.split(",")[0].split("/")
            tm = timestamp.split(",")[1].split(" ")[1].split(":")
            if int(tm[0]) != 12:
                hr = int(tm[0]) if timestamp[-2:] == "AM" else int(tm[0]) + 12
            else:
                hr = int(tm[0]) if timestamp[-2:] == "PM" else int(tm[0]) - 12
            return(datetime.datetime(int(dt[2]), int(dt[0]), int(dt[1]), hr, int(tm[1]), int(tm[2])))
        return("")
    
    def getAllDates(data: [], startDate):
        dates = []
        for timestamp in data:
            if(timestamp != ""):
                dt = timestamp.split(",")[0].split("/")
                date = datetime.date(int(dt[2]), int(dt[0]), int(dt[1]))
                if dates.count(date) == 0 and date >= startDate: dates.append(date)
        if len(dates) > 0:
            return(dates)
        else:
            return("")

    def dailyRecorded(data: [], date):
        stat = []
        if len(data) > 0:
            for arr in data:
                if len(arr) > 0 and arr[5] != "":
                    dbDate = datetime.date(arr[5].year,arr[5].month,arr[5].day)
                    if dbDate == date:
                        stat.append(arr[2])
            return(sum(stat))
        return(0)

    def dailyValidated(data: [], date, artist):
        stat = []
        if len(data) > 0:
            for arr in data:
                if len(arr) > 0 and arr[7] != "":
                    dbDate = datetime.date(arr[7].year,arr[7].month,arr[7].day)
                    if dbDate == date and arr[6] != artist and arr[4] != "":
                        stat.append(arr[2])
                        validatorsDaily.append(arr[6])
            return(sum(stat))
        return(0)

    recorded = []
    recordedHours = []
    accepted = []
    acceptedHours = []
    rejected = []
    rejectedHours = []
    notRecorded = []
    lastRecorded = []
    lastValidated = []
    data = []
    allDates = []
    startingRecordingNumber = 23501 if name == "tam-" else 0
    reportDate = datetime.datetime.today()
    totalUsable = 0
    for recording in range(len(content)):
        recordingNumber = int(content[recording]["recordingNumber"])
        recordingId = content[recording]["recordingId"]
        audioDuration = float(content[recording]["audioDuration"])
        status =  content[recording]["status"]
        voiceArtist = content[recording]["voiceArtist"]
        recordedDate = getDateAndTime(content[recording]["recordedDate"])
        validator = content[recording]["validator"]
        validatedDate = getDateAndTime(content[recording]["validatedDate"])
        if recordingNumber >= startingRecordingNumber:
            data.append([recordingNumber,recordingId,audioDuration,status,voiceArtist,recordedDate,validator,validatedDate])
            allDates.append(content[recording]["recordedDate"])
            if voiceArtist !="" and status == "accepted": validators.append(validator)
            if voiceArtist !="" and status == "rejected": validators.append(validator)
            if voiceArtist =="" and status == "accepted": pruned.append(validator)
            if voiceArtist =="" and status == "accepted": pruned.append(validator)
        if recordingNumber >= startingRecordingNumber and recordedDate != "": lastRecorded.append(recordedDate)
        if validatedDate != "" and validator != voiceArtist and status != "recorded" and recordingNumber >= startingRecordingNumber:
            lastValidated.append(validatedDate)
        if status == "recorded" and audioDuration > 0 and recordingNumber >= startingRecordingNumber:
            recorded.append(recordingId)
            recordedHours.append(audioDuration)
            totalUsable = totalUsable + audioDuration
        elif status == "accepted" and validator == voiceArtist and audioDuration > 0 and recordingNumber >= startingRecordingNumber:
            recorded.append(recordingNumber)
            recordedHours.append(audioDuration)
            totalUsable = totalUsable + audioDuration
        elif status == "accepted" and validator != voiceArtist and voiceArtist != "" and audioDuration > 0 and recordingNumber >= startingRecordingNumber:
            accepted.append(recordingId)
            recordedHours.append(audioDuration)
            acceptedHours.append(audioDuration)
            totalUsable = totalUsable + audioDuration
        elif status == "rejected" and audioDuration > 0 and voiceArtist != "" and recordingNumber >= startingRecordingNumber:
            rejected.append(recordingId)
            recordedHours.append(audioDuration)
            rejectedHours.append(audioDuration)
        else:
            if recordingNumber >= startingRecordingNumber: notRecorded.append(recordingId)
    lastRecorded.sort()
    if len(lastValidated)>0:
        lastValidated.sort(reverse=True)
    else:
        lastValidated.append("")
    if name != "tam-":
        splitDate = str(lastRecorded[0]).split(" ")[0].split("-")
        startingDate = datetime.date(int(splitDate[0]), int(splitDate[1]), int(splitDate[2]))
    else:
        startingDate = datetime.date(2023,8,21)
    rDate = datetime.date(reportDate.year,reportDate.month,reportDate.day-2)
    report = [["Total files", "Given files", 
               "To Be Validated", "Accepted files", "Rejected files", "To Be Recorded", "Report as on"],
              [totalLines[fileName[:3]], (len(recorded) + len(accepted) + len(rejected) + len(notRecorded)), 
                (len(recorded) + len(accepted) + len(rejected)), len(accepted), len(rejected), len(notRecorded), asOn]]
    workingDays = len(getAllDates(allDates, startingDate))
    totalDays = (tillDate - startingDate).days
    if workingDays > totalDays: workingDays = totalDays
    # rDate = datetime.date(2023,9,30)
    dV = dailyValidated(data, rDate, voiceArtist)
    
    df = pd.DataFrame(report[1] ,columns=[f"As on - {rDate}"])
    df.index = report[0]
    print(language[fileName[:3]])
    print(df)
    ax = plt.subplot(331,frame_on=False)
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    tbl = pd.plotting.table(ax, df, loc='center',)
    plt.title(f"{language[fileName[:3]]} Single Speaker TTS", fontsize = 10, y=1.2, x=0, fontweight = 25, fontdict= {'color':'Blue'})
    plt.savefig(filePath + language[fileName[:3]] + '_stats.jpg', bbox_inches = 'tight', dpi = 300)

print(f"Ramisha : {validators.count('malayalamvalidator@gmail.com')}")
print(f"Manoj : {validators.count('manoj@gmail.com')}")
print(f"Pranav : {validators.count('pranav@gmail.com')}")
print(f"Anjana : {validators.count('anjana@gmail.com')}")
print('')
print(f"Ramisha : {validatorsDaily.count('malayalamvalidator@gmail.com')}")
print(f"Manoj : {validatorsDaily.count('manoj@gmail.com')}")
print(f"Anjana : {validatorsDaily.count('anjana@gmail.com')}")