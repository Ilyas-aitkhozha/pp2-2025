def reverseStr(str):
    words = str.split()
    words.reverse()
    print(" ".join(words))

str = input("enter your sentence: ")
reverseStr(str)