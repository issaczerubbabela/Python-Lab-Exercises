'''Create a Python program that captures information about a person, including their name,
age, and address. Utilize tuple packing to store this information in a tuple, and then use
tuple unpacking to retrieve and display the information.'''

info = input("Enter name: "), input("Enter address: "), input("Enter age: ")
name, address, age = info
print('Your name is {}, your address is {} and your age is {}'.format(name, address, age))
