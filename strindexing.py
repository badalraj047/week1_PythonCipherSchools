# a = "Python"
# print(a[5])     #index 5 will be printed

# # string slicing
# a = "Python"
# print(a[1:3])      #index 1 to index 2 will be printed(stop argument is excluded)

# # step argument

# print("Badal"[0:5:2])       # here step argument is 2 so after P, a will pe printed
# print("Badal"[0::2])        # here there is no end argument so it will print till end but it will print paek
# print("Badal"[5::-1])       # here we have not put the end argument so it will start from 5th index and will print reverse from there as the step argument is -1   output= eetarp
# print("Badal"[::-1])        # it is used to reverse the string

#exercise
a = input("enter your name : ")
reverse = a[::-1]
print(f"reverse of your name is: {reverse}")