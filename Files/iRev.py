def RevText(file):
    with open(file,'r') as revFile:
        Input = revFile.read().split()
        for i in Input:
            if(i[0]=='i' or i[0]=='I'):
                print(i[::-1],end=' ')
            else: print(i,end=' ')

RevText('Story.txt')
