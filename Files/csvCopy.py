#Write a program to copy the data from "input.csv" to "input1.csv".

import csv
with open("input1.csv",'w') as file2:
    with open("input.csv",'r') as file1:
        reader = csv.reader(file1)
        writer = csv.writer(file2)
        for i in reader:
            writer.writerow(i)
