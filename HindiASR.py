from datetime import datetime
from numpy import intersect1d

st = datetime.now()
nw = st
# filenamesCSV = open('E:/IndiaSpeaks Research Labs/TTS/Single Speaker TTS/Hindi/Used File Names.csv','a+')
outputFile = open('E:/IndiaSpeaks Research Labs/TTS/Single Speaker TTS/Kannada/outputUniques.txt','w', encoding='utf8')
duplicateFile = open('E:/IndiaSpeaks Research Labs/TTS/Single Speaker TTS/Kannada/outputDup.txt','w', encoding='utf8')
dummyFile = open('E:/IndiaSpeaks Research Labs/TTS/Single Speaker TTS/Kannada/outputDummy.txt','w', encoding='utf8')
sourceFile = open('E:/IndiaSpeaks Research Labs/TTS/Single Speaker TTS/Kannada/All_Files.txt','r',encoding='utf8')
# oldFiles = filenamesCSV.readlines()
# duplicateFiles = []
# fileList = listdir(sourceFilePath)
# for file in fileList:
#     if oldFiles.count(file) > 1: duplicateFiles.append(file)
#     filenamesCSV.writelines(file)
contents = sourceFile.readlines()
compareLines = contents
sourceFile.close()
i = 0
dup = 0
for line in contents:
    # s = line.replace("a","").replace("b","").replace("c","").replace("d","").replace("e","").replace("f","").replace("g","")
    # s = s.replace("h","").replace("i","").replace("j","").replace("k","").replace("l","").replace("m","").replace("n","").replace("o","")
    # s = s.replace("p","").replace("q","").replace("r","").replace("s","").replace("t","").replace("u","").replace("v","").replace("w","")
    # s = s.replace("x","").replace("y","").replace("z","").replace("<","").replace(">","").replace("!","").replace("    "," ").replace("   "," ").replace("  "," ")
    # s = s.replace("A","").replace("B","").replace("C","").replace("D","").replace("E","").replace("F","").replace("G","")
    # s = s.replace("H","").replace("I","").replace("J","").replace("K","").replace("L","").replace("M","").replace("N","").replace("O","")
    # s = s.replace("P","").replace("Q","").replace("R","").replace("S","").replace("T","").replace("U","").replace("V","").replace("W","")
    # s = s.replace("X","").replace("Y","").replace("Z","")
    # l = s.strip(" ")
    
    i = i+1
    if line != "":
        a = line.strip().split(" ")
        for l in compareLines:
            if l != "":
                b = l.strip().split(" ")
                c = set(a).intersection(b)
                if len(c) >= (len(a)*0.9):
                    idx = contents.index(l)
                    dummyFile.writelines(l)
                    duplicateFile.writelines(f'{i}\t{len(a)}\t{len(c)}')
                    contents[idx] = ""
                    dup = dup + 1
        outputFile.writelines(line)
        compareLines = contents
    if (i % 1000) == 0:
        print(f"{i}\t{contents.count('')}\t{dup}\t{(datetime.now() - nw)}")
        nw = datetime.now()
        dup = 0
outputFile.close()
dummyFile.close()
duplicateFile.close()
print(datetime.now() - st)
