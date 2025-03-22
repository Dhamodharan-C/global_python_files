import os

error_file = []
path = '/home/damu/ISRL/ss_data_analysis/kannada/'
chk_files = os.listdir(path)

def validate(script: str, file: str, line_number: int):
    chk_num = ['0','1','2','3','4','5','6','7','8','9']
    chk_char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    chk_sym = ['~','`','!','@','#','$','%','^','&','*','(',')','-','_','=','+','{','}','[',']','|','\\','?','/','>','<']
    if script != "":
        for n in chk_num:
            if n in script and error_file.count(file + " " + str(line_number)) < 1: 
                error_file.append(file + " " + str(line_number))
        for c in chk_char:
            if c in script or c.upper() in script and error_file.count(file + " " + str(line_number)) < 1:
                error_file.append(file + " " + str(line_number))
        for s in chk_sym:
            if s in script and error_file.count(file + " " + str(line_number)) < 1:
                error_file.append(file + " " + str(line_number))

for file in chk_files:
    lines = open(path + file, 'r', encoding='utf8').readlines()
    i = 0
    for line in lines[2::3]:
        # space_1 = line.find(' ')
        # space_2 = line.find(' ', space_1 + 1)
        # validate(line[(space_2 + 1):], file, i)
        validate(line, file, i)
        i = i + 1
print(len(error_file))
# print(error_file)
erf = []
with open('/home/damu/ISRL/ss_data_analysis/errors/kannada.txt', 'w', encoding='utf8') as ef:
    for err in error_file:
        ref = str(err).split(" ")[0]
        if erf.count(ref) < 1:
            ef.writelines(ref + '\n')
            erf.append(ref)
print(erf)
