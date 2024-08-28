'''5. Get the input for principle amount, rate of interest and number of years. Calculate Simple interest and compound interest.'''
p,n,r = float(input("enter principal")),float(input("enter years")),float(input("enter rate"))
print("simple interest :",p*n*r/100.0)
print("compound interest:", p*pow(1+r,n))
                                              
