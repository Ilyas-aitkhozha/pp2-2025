import re

f = open("row.txt", 'r', encoding = "utf-8")
txt = f.read()
f.close()
#text = 'аббб'
find = r"аб{2,3}"
matches = re.search(find, txt)
if matches:
    print(matches.group(0))
else: 
    print("No string like this")