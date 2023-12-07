import json
from Report import Batch, Recording, getDateAndTime, getDate, oldVersionReport
import datetime

file = open('E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/Tamil/Validation Report.txt', 'w')
file.writelines(f"Speaker\tFilename\tValidator\tDate\tModified\tTotal Hours\tUsable hours\n")
adminDatas = open('C:/Users/damum/Downloads/tamil-tts.datas.json','r')
batches = json.load(adminDatas)
startingDate = datetime.date(2023,8,30)
for batch in range(len(batches)):
    B = Batch(batches[batch]["batchId"],batches[batch]["assignee"],len(batches[batch]["recordings"]),
              batches[batch]["correctedRecordingsCount"],batches[batch]["totalAudioDuration"],batches[batch]["usableAudioDuration"])
    for recording in range(B.recordings):
        R = Recording(batches[batch]["recordings"][recording]["recordingId"],batches[batch]["recordings"][recording]["recordingName"],
                      batches[batch]["recordings"][recording]["modifiedDate"],batches[batch]["recordings"][recording]["totalDuration"],
                      batches[batch]["recordings"][recording]["usableDuration"])
        if getDate(R.modified) != "":
                    if B.assignee[-14:] == "@validator.com": # and getDate(R.modified) > startingDate:
                        file.writelines(f"{B.id}\t{R.name}\t{B.assignee}\t{getDate(R.modified)}\t{getDateAndTime(R.modified)}\t{R.totalHours}\t{R.usableHours}\n")
file.close()
