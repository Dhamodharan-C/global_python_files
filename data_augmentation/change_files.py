import os

changeFiles = '/bkpdisk/webapp_backup/tamil_annotation/speech-annotation/Damu/change_files.txt'
# path = '/bkpdisk/webapp_backup/tamil_annotation/speech-annotation/server/data/original/'
path = '/bkpdisk/webapp_backup/tamil_annotation/speech-annotation/server/data/original/'
with open(changeFiles, 'r', encoding='utf8') as cF:
    errorFiles = cF.readlines()
chk = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','!','`','~','@','#','$',
       '%','^','&','*','(',')',',-','_','=','+','{','}','[',']',':',';','<','>','/','?','|','\\','0','1','2','3','4','5','6','7','8','9']
fileCount = 0
for efs in errorFiles:
    folder = efs.split('\t')[0]
    ef = efs.split('\t')[1].replace('\n','')
    print(ef)
    if os.path.exists(path + folder + '/' + ef):
        with open(path + folder + '/' + ef, 'r', encoding='utf8') as file:
            contents = file.readlines()
        newContents = []
        for content in contents:
            for i in chk:
                content = content.replace(i, ' ')
            content.replace('    ',' ').replace('   ', ' ').replace('  ', ' ').replace('  ', ' ').strip()
            newContents.append(content.split(' '))
        newContents.sort(key = lambda x: x[1])
        with open(path + folder + '/' + ef, 'w', encoding='utf8') as newFile:
            for newLine in newContents:
                l = ' '.join(newLine)
                l = l.strip() + '\n'
                newFile.writelines(l)
                fileCount += 1
print(fileCount)
