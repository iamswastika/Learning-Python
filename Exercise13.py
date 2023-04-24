#There is a range of numbers from 1 to 100. Now, taking a input from user. If the user input is less than the 
# number in the range, print "guess is low", if it's high, print "guess is high", else print "Congrats"

import random

x = random.randint(1, 100)

while True:
    userinp= int(input("Enter a number: "))

    if userinp>x:
        print("Your guess is high")
    elif userinp<x:
        print("Your guess is low")
    else:
        print("Congrats")
        break


    