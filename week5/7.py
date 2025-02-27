import re

def snake_to_camel(snake_str):
    while "_" in snake_str:
        find = re.search(r'_', snake_str)
        if find:
            index = find.start()
            snake_str = snake_str[:index] + snake_str[index + 1].upper() + snake_str[index + 2:]
    return snake_str

f = open("row.txt", 'r', encoding = "utf-8")
txt = f.read()
#text = "hELLO_wORLD_hOW_aRE_yOU"
#print(snake_to_camel(text))
f.close()
print(snake_to_camel(txt))
