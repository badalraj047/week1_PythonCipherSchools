# name = "Badal"
# age  = 19
# # print("hello {} your age is {}".format(name,age))         # output = hello Badal your age is 19 (p3)
# print(f"hello {name} your age is {age}")                    # f helps to print the format (p3.6)
#                                                             # output = hello Badal your age is 19   
#                                                             #{} this is container
                                                            
# a = input("enter the number: ")
# b = input("enter the number: ")
# c = input("enter the number: ")
a,b,c = (input("enter numbers: ")).split(",")                 # .split function is only used in strings
print(f"average is : {(int(a) + int(b) + int(c))/3}")
                                                  