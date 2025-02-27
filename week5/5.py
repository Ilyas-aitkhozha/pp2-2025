import re

f = open("row.txt", 'r', encoding = "utf-8")
txt = f.read()
f.close()
#text = 'im_daun hello how are you abob'
#find = r"\ba\w*b\b"
#text = 'абоба абоб'
find = r"\bа\w*б\b"
matches = re.search(find, txt)
if matches:
  print(matches.group())
else:
  print("no such string")