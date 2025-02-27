import re
f = open("row.txt", 'r', encoding = "utf-8")
txt = f.read()
f.close()
#text = 'СигмаБойСигмаБой'
find = re.sub(r'(\B[А-Я])',r'_\1', txt)
print(find)