#!/usr/bin/python3
class Tabs(object):

    def __init__(self,fname):
        #Symbols to be removed to preprocess tabs
        self.symbols = ['h','/','p','\\','*','^','|',"e","B","G","D","A","E"]

        self.a = []

        #MIDI equivalent of e B G D A E
        self.notes = [64, 59, 55, 50, 45, 40]

        self.fname = fname

    def preprocess(self):
        with open(self.fname) as f:
            content = f.readlines()

        content = [x.strip() for x in content]
        print("\n".join(content))
        print("\n")


        for symbol in self.symbols:
            for i,line in enumerate(content):
                content[i] = line.replace(symbol,"-")

        print("\n".join(content))

        for i,line in enumerate(content):
            self.a.append(line.split(" "))

        #print("\n\n\n\n")

        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
                #print(a[i][j],end="")
                if self.a[i][j]=='1':
                    if self.a[i][j+1] != '-':
                        self.a[i][j] = str(((int(self.a[i][j])*10) + int(self.a[i][j+1])))
                        self.a[i][j+1] = '-'

        self.displayTabs()

    def displayTabs(self):
        print("\n\n\n\n")
        for i in range(len(self.a[0])):
            for j in range(len(self.a)):
                print(self.a[j][i],end="")
            print()


    def convertNotes(self):
        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
                if self.a[i][j]!='-':
                    self.a[i][j] = str(int(self.a[i][j])+notes[i])

        self.displayTabs()
