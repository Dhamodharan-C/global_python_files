import os
import glob, shutil

folder = 'E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/New.tar/New/'
files = os.listdir(folder)
outFilePath = 'E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/Text.txt'
outFilePath2 = 'E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/Name.txt'
numberFiles = 'E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/number_files.txt'
changeFiles = 'E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/change_files.txt'
englishFiles = open('E:/IndiaSpeaks Research Labs/TTS/Multi Speaker TTS/english_files.txt', 'w', encoding='utf8')
# outFolder = 'E:/IndiaSpeaks Research Labs/TTS/Single Speaker TTS/Tamil/resample_trans/'
# files = open('E:/IndiaSpeaks Research Labs/TTS/Single Speaker TTS/Tamil/log_errors.txt', 'r', encoding='utf8')
# lines = files.readlines()
# for l in lines:
#     l = l.replace('\n', "")
#     file = folder + l
#     outFile = outFolder + l
    # shutil.copy(file, outFile)
nfCount = 0
cfCount = 0
outFile = open(outFilePath, 'a', encoding='utf8')
outFile2 = open(outFilePath2, 'a', encoding='utf8')
nf = open(numberFiles, 'a', encoding='utf8')
cf = open(changeFiles, 'a', encoding='utf8')
chk = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','!','`','~','@','#','$',
       '%','^','&','*','(',')',',-','_','=','+','{','}','[',']',':',';','<','>','/','?','|','\\']
for f in files:
    resample =  open(folder + f, 'r', encoding='utf8')
    contents = resample.readlines()
    resample.close()
    number_present = 0
    char_sym_present = 0
    for content in contents:
        outFile2.writelines(f + "\n")
        # resample = open(folder + f, 'w', encoding='utf8')
        # c = content.replace("&", " ").replace("-", " ").replace("*", " ").replace("?", " ").replace("!", " ").replace("~", " ").replace("  "," ").replace("  "," ")
        startPosition = content.find(" ", content.find(" ")+1)
        content = content[startPosition:].strip()
        for i in range(10):
            if content.find(str(i)) > 0:
                number_present += 1
        outFile.writelines(content + "\n")
    if number_present > 0:
        # nf.writelines(f + '\n')
        nfCount += 1
    else:
        for j in chk:
            if content.find(j) > 0:
                # cf.writelines(f + '\n')
                englishFiles.writelines(f + '\n')
                cfCount += 1
                break
outFile.close()
outFile2.close()
nf.close()
cf.close()
englishFiles.close()
print(nfCount)
print(cfCount)

