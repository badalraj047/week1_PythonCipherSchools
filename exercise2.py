winning_number = 10
guess_number = int(input("enter the number: "))
if winning_number == guess_number:
    print("YOU WIN !!!!")
else:
     if guess_number < winning_number:
        print("too low")    
     else:
         print("too high")     