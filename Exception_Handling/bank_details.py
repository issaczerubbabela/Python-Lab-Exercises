#Customer Details

import csv

def addCustDetails(bankDetails):
    while True:
        id = int(input("Enter Customer ID: "))
        name = input("Enter Customer Name: ")
        balance = int(input("Enter Customer Balance: "))
        bankDetails[id]={}
        bankDetails[id]['name'] = name
        bankDetails[id]['balance'] = balance
        ch = input("do you want to enter more customers(y/n): ")
        if ch=='n': break
    
def store_csv(file, bankDetails, defaulters):
    try:
        outfile=open(file,'w',newline='\n')
        writer = csv.writer(outfile)
        writer.writerow(['accno','name','balance'])
        for key in bankDetails.keys():
            if key>100:
                writer.writerow([key, bankDetails[key]['name'], bankDetails[key]['balance']])
            else: raise NameError
    except NameError:
        print("Account Number less than 100 ")
        defaulters.append([key, bankDetails[key]['name'], bankDetails[key]['balance']])
    finally:
        outfile.close()
        with open(file,'r',newline='\n') as readfile:
            reader = csv.reader(readfile)
            for i in reader:
                print(i)
        print(defaulters)
                
            

def main():
    defaulters=[]
    bankDetails={}
    addCustDetails(bankDetails)
    file = input("Enter the filename to store the account numbers more than 100: ")
    store_csv(file+'.csv',bankDetails,defaulters)
    
if __name__ == '__main__':
    main()
