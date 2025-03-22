import os

path = '/home/damu/ISRL/ss_data_analysis/tamil/voice_cloning/'
out_file = open(path + 'TamilPrompts.txt', 'w', encoding='utf8')
file_list = os.listdir(path + 'text/')
file_list.sort()
for file in file_list:
    with open(path + 'text/' + file, 'r', encoding='utf8') as in_file:
        text_string = in_file.readlines()[0]
        # print(file)
        out_file.writelines(text_string + '\n')
out_file.close()

