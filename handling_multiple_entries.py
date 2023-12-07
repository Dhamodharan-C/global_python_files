# multipleEntryFiles = 'E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/Tamil/Speaker wise Multiple Entries.txt'
multipleEntryFiles = '/bkpdisk/webapp_backup/tamil_annotation/speech-annotation/Damu/multipleEntries.txt'
# path = 'E:/IndiaSpeaks Research Labs/TTS/Single Speaker TTS/Malayalam/audioFiles/Recording samples/New/'
path = '/bkpdisk/webapp_backup/tamil_annotation/speech-annotation/server/data/original/'
mE = open(multipleEntryFiles, 'r', encoding='utf8')
errorFiles = mE.readlines()
# folders = ['sp_0692_revathi','sp_0694_devayani','sp_0701_drselvakumarcentumapp']
for entry in errorFiles:
    folder = entry.split('\t')[0]
    file = entry.split('\t')[1].replace('\n', '')
    with open(path + folder + '/' + file, 'r', encoding='utf8') as currentFile:
        lines = currentFile.readlines()
        # print(lines[0])
        lines_present = set()
        newLines = []
        for line in lines:
            line = line.strip()
            if line not in lines_present:
                newLine = line.split(' ')
                newLines.append(newLine)
                lines_present.add(line)
        newLines.sort(key = lambda x: x[1])
    with open(path + folder + '/' + file, 'w', encoding='utf8') as newFile:
        for nl in newLines:
            l = ' '.join(nl)
            l = l.strip() + '\n'
            newFile.writelines(l)
