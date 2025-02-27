import re
f = open("row.txt", 'r', encoding = "utf-8")
txt = f.read()
f.close()
#text = 'Аб'
find = 'аб*'
matches = re.search(find, txt)

print(matches.group(0))
