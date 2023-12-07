from os import listdir, rename

txtPath =  'C:/Users/damum/Downloads/srt/now'

txtFilenames = listdir(txtPath)
outFile = open('OUTPUT.txt','w')
for txtFilename in txtFilenames:
    newTextName = txtFilename.replace("(1)","").replace("(2)","").replace(".SRT","").replace(" ","").replace("(3)","")
    rename((txtPath+"/"+txtFilename), (txtPath+"/"+newTextName))
    outFile.writelines(newTextName + "\n")
outFile.close()

# audioPath = 'D:/Temporary Folder/Test/Audio Files/'
# audioFilenames = os.listdir(audioPath)
# for audioFilename in audioFilenames:
#     newAudioName = audioFilename.replace('TTS_012_SP','TTS_001_SP')
#     os.rename((audioPath+audioFilename), (audioPath+newAudioName))
    # audioFile.write(audioFilename+"\t"+newAudioName+"\n")

# txtFile.close()
# audioFile.close()