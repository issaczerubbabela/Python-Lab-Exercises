#Write a program to search the record from "input.csv" according to the register
#number input from the user. Structure of record saved in "input.csv" is Reg_no,
#Name, Year, Section, Tot_marks.
import csv
reg = input("Enter the register number to be searched: ")
with open("input.csv",'r') as record:
    reader=csv.reader(record)
    for i in reader:
        if(i[0]==reg):
            print(i)
            break
    else: print("Not Found")
