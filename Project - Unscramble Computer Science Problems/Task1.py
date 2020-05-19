"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    num_list1=[]
    for t in texts:
        num_list1.extend([t[0],t[1]])
    short_list1 = dict.fromkeys(num_list1)
   

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    num_list2=[]
    for c in calls:
        num_list2.extend([c[0],c[1]])
    short_list2 = dict.fromkeys(num_list2)

short_list1.update(short_list2)

print(f"There are {len(short_list1)} different telephone numbers in the records. ")
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
