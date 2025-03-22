import csv
from os import listdir


csv_file_path = 'C:/Users/damum/Downloads/Malayalam news dataset.csv'
txt_file_path = 'C:/Users/damum/Downloads/Output Malayalam.txt'
count = 0
length = 0

# allFiles = listdir(csv_file_path)
# for csvFile in allFiles:
#     print(csvFile)
with open(csv_file_path, 'r', encoding= 'utf8') as file:
    csv_reader = csv.reader(file)
    data_list = []
    for row in csv_reader:
        entry = row[1].strip().split(". ")
        for r in entry:
            data_list.append(r + ".")
with open(txt_file_path, 'w', encoding= 'utf8') as outFile:
    for line in data_list:
        if len(line) >= 85 and len(line) <= 130:
            s = line.replace("a","").replace("b","").replace("c","").replace("d","").replace("e","").replace("f","").replace("g","")
            s = s.replace("h","").replace("i","").replace("j","").replace("k","").replace("l","").replace("m","").replace("n","").replace("o","")
            s = s.replace("p","").replace("q","").replace("r","").replace("s","").replace("t","").replace("u","").replace("v","").replace("w","")
            s = s.replace("x","").replace("y","").replace("z","").replace("<","").replace(">","").replace("!","").replace("    "," ").replace("   "," ").replace("  "," ")
            s = s.replace("A","").replace("B","").replace("C","").replace("D","").replace("E","").replace("F","").replace("G","")
            s = s.replace("H","").replace("I","").replace("J","").replace("K","").replace("L","").replace("M","").replace("N","").replace("O","")
            s = s.replace("P","").replace("Q","").replace("R","").replace("S","").replace("T","").replace("U","").replace("V","").replace("W","")
            s = s.replace("X","").replace("Y","").replace("Z","").replace("-"," ").replace("  "," ").replace("  "," ").replace("..",".")
            l = s.replace("..",".").replace("\n", "").strip(" ")
            outFile.writelines(l + '\n')
            count += 1
            if len(l) > length: length = len(l)
print(count)
print(length)

# .replace("। ","।\n")
# import json
 
# def csv_to_json(csvFilePath, jsonFilePath):
#     jsonArray = []
      
#     #read csv file
#     with open(csvFilePath, encoding='utf-8') as csvf: 
#         #load csv file data using csv library's dictionary reader
#         csvReader = csv.DictReader(csvf) 

#         #convert each csv row into python dict
#         for row in csvReader: 
#             #add this python dict to json array
#             jsonArray.append(row)
  
#     #convert python jsonArray to JSON String and write to file
#     with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
#         jsonString = json.dumps(jsonArray, indent=4)
#         jsonf.write(jsonString)

#read csv file

## def isNotNumber(entry: str):
##     numList = [1,2,3,4,5,6,7,8,9,0]
##     for i in numList:
##         if entry.find(str(i)) >= 0:
##             return False
##     return True

## csvFilePath = 'C:/Users/damum/Downloads/train.csv/train.txt'
## txtFilePath = 'C:/Users/damum/Downloads/train.csv/Tamil SS TTS Source Data.txt'
## txtFile = open(txtFilePath, 'w', encoding='utf-8')
## with open(csvFilePath, encoding='utf-8') as csvf: 
##     #load csv file data using csv library's dictionary reader
##     csvReader = list(csvf.readlines())
##     for line in csvReader:
##         if len(line) >= 75 and len(line) <= 150 and isNotNumber(line):
##             txtFile.writelines(line)
## txtFile.close()
