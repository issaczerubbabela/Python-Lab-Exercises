#write a program in python to display first line from the file data.txt

with open('data.txt','r') as file:
    print(file.readline())
