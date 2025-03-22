# transFiles = 'E:/IndiaSpeaks Research Labs/TTS/Single Speaker TTS/Tamil/textFiles/transFiles.txt'
# filenames = 'E:/IndiaSpeaks Research Labs/TTS/Single Speaker TTS/Tamil/textFiles/recordingNames.txt'
# checkFiles = 'E:/IndiaSpeaks Research Labs/TTS/Single Speaker TTS/Tamil/textFiles/checkFiles.txt'
# outFile = 'E:/IndiaSpeaks Research Labs/TTS/Single Speaker TTS/Tamil/textFiles/errorFiles.txt'

# checkContents = open(checkFiles, 'r', encoding="utf8")
# cc= checkContents.readlines()
# transContents = open(transFiles, 'r', encoding="utf8")
# tc = transContents.readlines()
# files = open(filenames, 'r', encoding="utf8")
# fs = files.readlines()
# out = open(outFile, 'a', encoding="utf8")

# for line in cc:
#     if tc.count(line) > 0:
#         index = tc.index(line)
#         f = fs[index].replace("\n", "")
#         out.writelines(f"{f}\t{tc[index]}") 

# checkContents.close()
# transContents.close()
# files.close()
# out.close()


# checkFiles = 'E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/Tamil Multispeaker TTS/trans.tar/checkFiles2.txt'
# path = 'E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/Tamil Multispeaker TTS/trans.tar/Errors/'
# file = open(checkFiles, 'r', encoding='utf8')
# filenames = []
# fileCount = 0
# cf = file.readlines()
# for k in cf:
#     l = k.split("\t")
#     if filenames.count(l[0]) == 0: filenames.append(l[0])
# print(len(filenames))
# for f in filenames:
#     outFile = open(path + f + '.txt','w', encoding='utf8')
#     for i in cf:
#         line = i.split("\t")
#         if line[0] == f:
#             outFile.writelines(line[1])
#             fileCount += 1
#     outFile.close()
# print(fileCount)

transFilesPath = 'E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/original/'
multipleEntries = 'E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/Tamil/Multiple Entries.txt'
outFile = 'E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/RemoveFiles.txt'
out = open(outFile, 'w', encoding='utf8')
with open(multipleEntries, 'r', encoding='utf8') as mE:
    me_Files = mE.readlines()
    files = []
hrs = 0
for f in me_Files:
    file = f.split('\t')[0].replace('.wav', '.txt')
    duration = round(float(f.split('\t')[3]),1)
    with open(transFilesPath + file, 'r', encoding='utf8') as tempFile:
        lines = tempFile.readlines()
    actualDuration = 0
    for line in lines:
        start = float(line.split(' ')[0])
        end = float(line.split(' ')[1])
        actualDuration = round((end - start),1) + actualDuration
    print(f"{actualDuration}\t{duration}")
    if (actualDuration-duration)>1 or (duration-actualDuration)>1:
        out.writelines(f"{file}\n")
        hrs = hrs + duration
print(hrs/3600)