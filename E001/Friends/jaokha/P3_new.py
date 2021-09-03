"""
P3. EEG.
Student name: Thiranat Kanchanophat
"""

File_name = input("File: ")
series = input("Series: ")
series = series.split(" ")
answer_list = []
with open(File_name, 'r') as f:
    s = f.readlines()
    for item in s:
        item = item.split(" ")
        if item[0] == series[0] and item[1] == series[1]:
            add_item = item[3].strip()
            answer_list.append(float(add_item))

print(answer_list)

f.close()
