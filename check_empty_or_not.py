#check empty or not
#important
name = "abc"
if name:                #true if string is not empty
    print("string is not empty")        #output = string is not empty
else:
    print("string is empty")   
  
  
name = ""  
if name:                #true if string is not empty
    print("string is not empty")
else:
    print("string is empty")         #output = string is empty
    
name = input("enter your name : ")          # if you enter your name you will get output what you have entered
if name:                                    #if you did not  enter anything then the output will be you didn't type anything   
    print(f"your name is {name}")
else:
    print("you didn't type anything")
            
  
      