def palindrome(str):
    str = str.replace(" ", "").lower()
    return str == str[::-1]
str = input("enter your phrase or word: ")
if palindrome(str):
    print(True)
else:
    print(False)