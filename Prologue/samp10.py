'''4. Develop a Python code to determine if a given string is a palindrome. Ignore spaces,  punctuation, and capitaliza7on in the comparison.'''
while True:
    a = input('enter a string :')
    if(a.lower() == a.lower()[-1::-1]):
        print('its a palindrome')
    else:
        print('its not a palindrome')
