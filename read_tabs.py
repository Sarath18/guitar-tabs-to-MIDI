#!/usr/bin/python3

def main():
    fname = "/home/sarath/tabs_to_midi/tab.txt"
    symbols = ['h','/','p','\\','*','^','|',"e","B","G","D","A","E"]
    with open(fname) as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    print("\n".join(content))
    print("\n")


    for symbol in symbols:
        for i,line in enumerate(content):
            content[i] = line.replace(symbol,"-")

    print("\n".join(content))

    a = []

    for i,line in enumerate(content):
        a.append(line.split(" "))

    #print("\n\n\n\n")

    for i in range(len(a)):
        for j in range(len(a[i])):
            #print(a[i][j],end="")
            if a[i][j]=='1':
                if a[i][j+1] != '-':
                    a[i][j] = str(((int(a[i][j])*10) + int(a[i][j+1])))
                    a[i][j+1] = '-'

    print("\n\n\n\n")
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j],end="")
        print()


if __name__ == '__main__':
    main()
