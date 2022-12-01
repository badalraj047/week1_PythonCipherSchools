#string can only be added to string
#strings are immutable
a = "Badal"
b = "Raj"
# print(a+" "+b)    # output = Badal Raj
print(a+str(3))     # 3 is converted to string, output = Badal(3)
print(a*3)          # output = BadalBdalBadal