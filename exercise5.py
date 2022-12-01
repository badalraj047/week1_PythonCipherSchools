# ask user a number like 1234
#calculate sum of digits ---> 1+2+3+4
n =  input("enter a number : ")
total = 0
i = 0
while i < len(n):
    total += int(n[i])
    i += 1
print(total)    
