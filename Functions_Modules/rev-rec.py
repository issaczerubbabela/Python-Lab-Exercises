def reverse_string_odd(string, i, j):
    if i >= j:
        return True
    if string[i] != string[j]:
        return False
    return reverse_string_odd(string, i - 1, j + 1)

def reverse_string_even(string, i, j):
    if i > j:
        return True
    if string[i] != string[j]:
        return False
    return reverse_string_even(string, i - 1, j + 1)

string = input('Enter a string: ')
result = reverse_string_odd(string, -1, 0) if len(string) % 2 != 0 else reverse_string_even(string, -1, 0)
if result:
    print('Palindrome')
else:
    print('Not a palindrome')
