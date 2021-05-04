class abc:
    x = ""
    def getString(self):
        print("Enter the string")
        self.x = input()
    def printString(self):
        print(self.x.upper())


a = abc()
a.getString()
a.printString()
