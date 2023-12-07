from datetime import datetime, timedelta
from os import listdir
from glob import glob

num_files = []
char_files = []
sym_files = []
na_files = []

def validate(script: str, file: str, zone: int, st: str, et: str):
    chk_num = ['0','1','2','3','4','5','6','7','8','9']
    chk_char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    chk_sym = ['~','`','!','@','#','$','%','^','&','*','(',')','-','_','=','+','{','}','[',']','|','\\','?','/','>','<']
    if script != "<NA>" or script != "":
        for n in chk_num:
            if n in script: 
                num_files.append(f"{file.replace('.srt','')}_{str(zone).zfill(4)}\t{st}\t{et}")
                break
        for c in chk_char:
            if c in script or c.upper() in script:
                char_files.append(f"{file.replace('.srt','')}_{str(zone).zfill(4)}\t{st}\t{et}")
                break   
        for s in chk_sym:
            if s in script:
                sym_files.append(f"{file.replace('.srt','')}_{str(zone).zfill(4)}\t{st}\t{et}")
                break
        return True
    else:
        na_files.append(f"{file.replace('.srt','')}_{str(zone).zfill(4)}\t{st}\t{et}")
        return False

path = '/home/damu/Downloads/srt/hi_0001_rahulgandhi/'
err_folder = "/home/damu/ISRL/Hindi_MS/rahul_gandhi/errors/"
text_file_folder = "/home/damu/ISRL/Hindi_MS/rahul_gandhi/segmented_text_files/"
outputFile = open("/home/damu/ISRL/Hindi_MS/rahul_gandhi/database.txt","w")

audioMetadata = {}
actualAudioDurations = open("/home/damu/ISRL/Hindi_MS/rahul_gandhi/audio_length.txt","r")
audioData = actualAudioDurations.readlines()
actualAudioDurations.close()
print(audioData)
for line in audioData:
    audioLength, audioName = line.partition("\t")[::2]
    audioMetadata[audioName.replace("\n","")[:-4]] = audioLength[:7]

# subFolders = glob(path + "*", recursive = True)
outputFile.writelines(f"File\tActual Duration\tUsable Duration\tZones\tMax\tMin\n")
totalUsable = timedelta()
totalDuration = timedelta()
# for folder in subFolders:
    # user = folder[(len(path)):]
fileList = listdir(path)
for file in fileList:
    fileName = path + file
    # fileName = f"{path}/{user}/{file}"
    txtFile = open(fileName,"r")
    content = txtFile.readlines()
    txtFile.close()
    file = file.replace("(1)","").replace("(2)","").replace(".SRT","").replace(" ","").replace("(3)","")
    actualDuration = audioMetadata[file[:-4]]
    zonesOutOfRange = []
    allVal = []
    secondsTotal = 0
    usableDuration = timedelta()
    fileDuration = datetime.strptime(actualDuration, '%H:%M:%S')
    print(file)
    c = 1
    for i in range(1,(len(content)),4):
        chk = validate(content[i+1], file, c, content[i][0:8], content[i][-13:-5])
        text_file_name = text_file_folder + (file.replace(".srt", "")) + '_' + str(c).zfill(4) + '.txt'
        with open(text_file_name, 'w', encoding='utf8') as text_file:
            text_file.writelines(content[i+1])
        c = c + 1
        # chk = True
        if chk == True:
            startTime = datetime.strptime(content[i][0:8], '%H:%M:%S')
            endTime = datetime.strptime(content[i][-13:-5], '%H:%M:%S')
            val = (endTime-startTime).seconds
            usableDuration = usableDuration + (endTime-startTime)
            allVal.append(val)
            secondsTotal = secondsTotal + val
    outputFile.writelines(f"{file}\t{actualDuration}\t{usableDuration}\t{len(allVal)}\t{max(allVal)}\t{min(allVal)}\n")
    # outputFile.writelines(f"{file}\t{usableDuration}\t{len(allVal)}\t{max(allVal)}\t{min(allVal)}\n")
    totalUsable = totalUsable + timedelta(seconds=secondsTotal)
    # totalDuration = totalDuration + fileDuration
outputFile.close()
with open(err_folder + 'num.txt', 'w', encoding='utf8') as num:
    for x in num_files:
        num.writelines(x + '\n')
with open(err_folder + 'char.txt', 'w', encoding='utf8') as char:
    for j in char_files:
        char.writelines(j + '\n')
with open(err_folder + 'sym.txt', 'w', encoding='utf8') as sym:        
    for k in sym_files:
        sym.writelines(k + '\n')
with open(err_folder + 'na.txt', 'w', encoding='utf8') as na:        
    for l in na_files:
        na.writelines(l + '\n')

print(totalDuration)
print(totalUsable)
print(f"Numbers : {len(num_files)}")
print(f"English : {len(char_files)}")
print(f"Symbols : {len(sym_files)}")
print(f"<NA>    : {len(na_files)}")

# print(len(allVal))
