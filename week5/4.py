import re

f = open("row.txt", 'r', encoding = "utf-8")
txt = f.read()
f.close()
find = r"[А-Я]{1}[а-я]+"
matches = re.findall(find, txt)
print(matches)