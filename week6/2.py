string = input("Enter string: ")
uppercount = 0
lowercount = 0
for i in string:
    if i.isupper():
        uppercount+=1
    elif i.islower():
        lowercount+=1
print(f"upper letters in sentence:{uppercount}, and lower:{lowercount}")
