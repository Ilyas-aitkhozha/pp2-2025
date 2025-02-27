import re
f = open("row.txt", 'r', encoding = "utf-8")
txt = f.read()
f.close()
#text = 'ПриветЯПодсяду'
find = re.sub(r'(?=[А-Я])', ' ', txt)
print(find)