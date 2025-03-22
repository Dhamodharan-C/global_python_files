from os import listdir

lang = "malayalam"
txt_folder = "/home/damu/Downloads/ss_tts/" + lang + "/"
out_folder = "/home/damu/Downloads/ss_tts/" + lang + "_errors/"
file_list = listdir(txt_folder)
chk_num = ['0','1','2','3','4','5','6','7','8','9']
chk_char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
chk_sym = ['~','`','!','@','#','$','%','^','&','*','(',')','-','_','=','+','{','}','[',']','|','\\','?','/','>','<']
num_files = []
char_files = []
sym_files = []
for filename in file_list:
    file = open(txt_folder + filename, 'r', encoding= 'utf8')
    content = file.readline()
    for n in chk_num:
        if n in content: 
            num_files.append(filename)
            break
    for c in chk_char:
        if c in content or c.upper() in content:
            char_files.append(filename)
            break
    for s in chk_sym:
        if s in content:
            sym_files.append(filename)
            break
with open(out_folder + 'num.txt', 'w', encoding='utf8') as num:
    for i in num_files:
        num.writelines(i + '\n')
with open(out_folder + 'char.txt', 'w', encoding='utf8') as char:
    for j in char_files:
        char.writelines(j + '\n')
with open(out_folder + 'sym.txt', 'w', encoding='utf8') as sym:        
    for k in sym_files:
        sym.writelines(k + '\n')
    
print(f"Numbers : {len(num_files)}")
print(f"English : {len(char_files)}")
print(f"Symbols : {len(sym_files)}")