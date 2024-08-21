#caesar cipher

a = input("Enter the text to be encrypted: ")
encrypt = ''
for i in a:
    encrypt+=chr(ord(i)+3)
print(list([a, encrypt, ''.join([chr(ord(i)-3) for i in encrypt])]))
