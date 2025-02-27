import re

f = open("row.txt", 'r', encoding = "utf-8")
txt = f.read()
f.close()
#text = 'я_учу'
find = r"[а-я]+_[а-я]+"
matches = re.findall(find,txt)
print(matches)