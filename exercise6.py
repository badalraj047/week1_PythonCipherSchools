# to take a input from user and print how many times the letter has been appeared in input
name = input("enter your name : ")
b = ""
i = 0
while i < len(name):
    if name[i] not in b:
        b += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1
    
