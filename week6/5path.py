f = open("hello.txt", "a")
lst = ["yeah im a list"]
f.write(f"\nnow u have list {lst}")
f.close()

f = open("hello.txt", "r")
lines = f.readlines()
f.close()
"""
new = []
for line in lines:
    if "now u have list" not in line:
        new.append(line)

f = open("hello.txt", "w")
f.writelines(new)
f.close()
"""
f = open("hello.txt", 'r')
print (f.read())