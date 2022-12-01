name,char = input("enter your name and character :").split(",")         #it will take two inputs separated by comma
print("length of your name is:",len(name))                              #it will print length of your name
print(f"chacacter count : {name.strip().lower().count(char.strip().lower())}")           #it will print the count of your character input
