import re
f = open("row.txt", 'r', encoding = "utf-8")
txt = f.read()
f.close()
#text= "как ты думаешь это получилось, или нет."
find = re.sub(r'[ ,.]', ":",txt)
print(find)