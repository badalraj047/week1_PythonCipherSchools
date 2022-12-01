#take two inputs from user name and age
#if age is > 10 and username starts with "a" or "A" print "you can watch coco"
#else print "you cannot watch coco"
username = input("enter your name: ")
age = int(input("enter your age: "))
if age >= 10 and (username[0] == "a" or username[0] == "A"):
    print("you can watch coco")
else:
    print("you cannot watch coco")    