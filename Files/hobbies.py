#Accept five hobbies from the user and write in a file "hobbies.txt"

hobbies=[]
for i in range(5):
    a = input("Enter the name of the fruit "+str(i+1)+": ")
    hobbies.append(a+'\n')

with open('hobbies.txt','w',newline='\n') as fruitfile:
    fruitfile.writelines(hobbies)
