basic = int(input('enter basic pay'))
print('gross :', basic*1.15, file = open("new.txt",'w'))
print('net :', basic*1.15*0.98, file = open("new.txt",'a'))
