import re
f = open("row.txt", 'r', encoding = "utf-8")
txt = f.read()
f.close()
#text  = 'ЯлюблюЭтотМирАбоба'
find = re.split(r'(?=[А-Я])', txt)
print(find)