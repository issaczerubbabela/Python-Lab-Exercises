def palindrome(string):
    if string[::-1] == string:
        print("the strings represent each other in the reverse order.")
    else:
        print(" the strings do not represent each other in the reverse order.")
    for i in string[::-1]:
        print(i)
palindrome(input("Enter a string: "))

def vowel_count(string):
    return sum([string.count(vowel) for vowel in ['a', 'e', 'i', 'o', 'u']])

def 
