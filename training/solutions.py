#Print unique values as a list from a given list using for loop.
list1 = [1,5,10,15,20,25,30,35,40,10,20,30,40,50,60]
unique_values = []
for item in list1:
    if item not in unique_values:
        unique_values.append(item)
print(unique_values)

#Print unique lastnames as a list from a given list of players.
list2 = ["Rohit Sharma", "Virat Kohli", "Shreyas Iyer", "Shubman Gill", "Ishant Sharma", "Ravindra Jadeja", "Venkatesh Iyer"]
unique_last_names = []
for name in list2:
    last_name = name.split(" ")[-1]
    if last_name not in unique_last_names:
        unique_last_names.append(last_name)
print(unique_last_names)

#Print the sum of alphabetical orders of "INDIA".
list3 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
word = "INDIA"
score = 0
for letter in word:
    score += (list3.index(letter) + 1)
print(score)

#