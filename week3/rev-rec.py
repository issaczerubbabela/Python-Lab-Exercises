def reverse_string_odd(string, i, j):
    while (i+len(string))!=j:
        if string[i]!=string[j]:
            return False
        i=i-1
        j=j+1
    return True
def reverse_string_even(string, i, j):
    while (i+len(string))-1 == j:
        if string[i]!=string[j]:
            return False
        i=i-1
        j=j+1
    return True
string = input('enter a string')
result = reverse_string_odd(string,-1,0) if len(string)%2!=0 else reverse_string_even(string,-1,0)
if result:
    print('palindrome')
else: print('not palindrome')
