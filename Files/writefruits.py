#Accept five fruit names from the user and write in a file "fruits.txt"

fruits=[]
for i in range(5):
    a = input("Enter the name of the fruit "+str(i+1)+": ")
    fruits.append(a)

with open('fruits.txt','w',newline='\n') as fruitfile:
    for fruit in fruits:
        fruitfile.write(fruit+'\n')
