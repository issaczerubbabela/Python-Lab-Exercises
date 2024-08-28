
bmi = float(input("enter weight: ")) / float(input("enter height: "))**2
print ('Underweight') if bmi < 18.5 else print ('Normal Weight') if bmi < 25 else print ('Overweight') if bmi>=25 else print ('Obese')
