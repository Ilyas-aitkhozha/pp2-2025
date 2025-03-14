f = open("hello.txt", "r")
count = 0
for i in f:
    count+=1
f.close()
print(count)
