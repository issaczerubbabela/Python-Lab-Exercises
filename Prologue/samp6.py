'''6. Read 5 subject marks as input. Calculate total and average for that particular student.'''
a,b,c,d,e = [int(x) for x in input("Enter five values: ").split()]#map(int, input('enter the marks in five subjects: ').split())
print('total:',a+b+c+d+e,'mean:',float(a+b+c+d+e)/5)
