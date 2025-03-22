import datetime
import math


class Batch:
    def __init__(self, id: str, assignee: str, recordings: int, completed: int, totalHours: str, usableHours: str) -> None:
        self.id = id
        self.assignee = assignee
        self.recordings = recordings
        self.completed = completed
        self.totalHours = totalHours
        self.usableHours = usableHours


class Recording:
    def __init__(self, id: str, name: str, modified: str, totalHours: str, usableHours: str) -> None:
        self.id = id
        self.name = name
        self.modified = modified
        self.totalHours = totalHours
        self.usableHours = usableHours


def getDateAndTime(timestamp: str):
    if(timestamp != ""):
        mon = ['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        dt = timestamp.split(" ")
        out = dt[4].split(":")
        dtOut = datetime.datetime(int(dt[3]),int(mon.index(dt[1])),int(dt[2]),int(out[0]),int(out[1]),int(out[2]))
        tOut = dtOut + datetime.timedelta(hours=5, minutes=30, seconds=0)
        return(datetime.datetime(tOut.year,tOut.month,tOut.day,tOut.hour,tOut.minute,tOut.second))
    return("")

def getDate(timestamp: str):
    if(timestamp != ""):
        mon = ['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        dt = timestamp.split(" ")
        out = dt[4].split(":")
        dtOut = datetime.datetime(int(dt[3]),int(mon.index(dt[1])),int(dt[2]),int(out[0]),int(out[1]),int(out[2]))
        tOut = dtOut + datetime.timedelta(hours=5, minutes=30, seconds=0)
        outDate = str(tOut).split(" ")
        outDate = outDate[0].split("-")
        return(datetime.date(int(outDate[0]),int(outDate[1]),int(outDate[2])))
    return("")

def getHoursInDecimal(HourValue):
    if type(HourValue) != int:
        HourValue = round(HourValue,2)
        hr = math.floor(HourValue)
        mn = int((HourValue - float(hr))*60.00)/100
        return(hr + mn)
    else:
        return(HourValue)

def oldVersionReport(filename: str):
    file = open(filename, 'r')
    db = file.readlines()
    file.close()
    dbDict = {}
    for line in db:
        dbValue = (line.replace('\n','').split(','))
        dbDict[dbValue[4]] = dbValue
    return dbDict

# def honey(userdata: []):
#     if len(userdata) > 0:
#         for

# print(getDateAndTime("Thu Jun 29 2023 21:18:22 GMT+0000 (Coordinated Universal Time)"))
# print(len(oldVersionReport('E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/Tamil/Transcription Database.txt')))