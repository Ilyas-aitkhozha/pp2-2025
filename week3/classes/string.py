class Strings:
    def getString(self):
            self.text = input("Enter a string: ")
    def printString(self):
          print(self.text.upper())
r1 = Strings()
r1.getString()
r1.printString()