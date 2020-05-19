"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

bang=[]
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
      if call[0].startswith('(080)'):
        bang.append(call[1])


fix=[]
tele=[]
mob=[]

for b in bang:
  if b.startswith('('):
    i=b.find(')')
    fix.append(b[:i+1])
  else:
    if b.startswith('140'):
      tele.append(b[:3])
    else:
       mob.append(b[:4])
       
lfinal=fix+tele+mob
lfinal=set(lfinal)
lfinal = list(lfinal)
lfinal.sort()
print("The numbers called by people in Bangalore have codes:")
for s in lfinal:
  print(s)

b_to_b = []
for b in bang:
  if '(080)' in b:
    b_to_b.append(b)

count_btb = len(b_to_b)
count_bta = len(bang)

percent = count_btb/count_bta*100
print(f"{percent:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")



"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
