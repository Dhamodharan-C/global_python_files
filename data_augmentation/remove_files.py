import shutil,os
# multiple_entries, null_entries, number_files

removeFiles = '/bkpdisk/webapp_backup/tamil_annotation/speech-annotation/Damu/RemoveFiles.txt'
numberFiles = '/bkpdisk/webapp_backup/tamil_annotation/speech-annotation/Damu/number_files.txt'
# path = '/bkpdisk/webapp_backup/tamil_annotation/speech-annotation/server/data/original/'
path = '/bkpdisk/webapp_backup/tamil_annotation/speech-annotation/server/data/original/'
RemovedFilesPath = '/bkpdisk/webapp_backup/tamil_annotation/speech-annotation/Damu/RemovedFiles/'
NumberFilesPath = '/bkpdisk/webapp_backup/tamil_annotation/speech-annotation/Damu/NumberFiles/'
rfCount = 0
nfCount = 0
with open(removeFiles, 'r', encoding='utf8') as rF:
    remFiles = rF.readlines()
with open(numberFiles, 'r', encoding='utf8') as nF:
    numFiles = nF.readlines()
for r in remFiles:
    folder = r.split('\t')[0]
    rm = r.split('\t')[1].replace('\n', '')
    if os.path.exists(path + folder + '/' + rm):
        shutil.move(path + folder + '/' + rm, RemovedFilesPath)
        rfCount += 1
for n in numFiles:
    folder = n.split('\t')[0]
    nu = n.split('\t')[1].replace('\n', '')
    if os.path.exists(path + folder + '/' + nu):
        shutil.move(path + folder + '/' + nu, NumberFilesPath)
        nfCount += 1
print(f'removed : {rfCount}')
print(f'numbers : {nfCount}')

