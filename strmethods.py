# len function
a = "Badal"
print(len(a))       #it will print the length of your sting

# lower() method
a = "BaDaL"
print(a.lower())     #it will print all the characters in lowercase

#upper() method
a = "badal"
print(a.upper())     #it will print all the characters in uppercase

#title() method
a = "bAdaL"
print(a.title())     #it will convert the first letter to uppercase and rest to lowercase

#count() method
a = "The butter i bought is better butter"
print(a.count("butter"))      #it will make a count of butter in the string

#replace() method
a = "The journey of 1000 sleepless nights starts with hello world"
print(a.replace(" ","_",1))      #it will replace all the spaces with underscore(_) and 1 represnts that only 1 space will be rplaced by underscore(_) starting from begginng

#find() method
a = "The journey of 1000 sleepless nights starts with hello world"
print(a.find("hello"))           #it will print the positon of word or letter