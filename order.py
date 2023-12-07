import os
audioPath =  'D:/Temporary Folder/Test/Audio Files/'
textPath =  'D:/Temporary Folder/Test/Text Files/'
audioFiles = os.listdir(audioPath)
textFiles = os.listdir(textPath)
for audioFile in audioFiles:
    textPosition = textFiles.index(audioFile.replace("/Audio Files/","/Text Files/").replace(".wav",".txt"))
    textFile = textFiles[textPosition]
    
