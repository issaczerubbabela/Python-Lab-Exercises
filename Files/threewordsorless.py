def ShowWords(file):
    with open(file,'r') as wordFile:
        words = wordFile.read().split()
        for i in words:
            if(len(i)<3): print(i)
ShowWords('newfile.txt')
