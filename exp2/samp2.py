#password strength
pwd = input("enter password: ")

print('weak') if len(pwd)<8 else print('strong') if any(char in pwd for char in '!@#$%^&*(),.?":{}|<>') else print("moderate")
