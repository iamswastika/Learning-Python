#Rewrite the program using try and except so that your program handles non-numerix input gracefully printing the message and exiting the program

hour=input("Enter the hour: ")
rate =input("Enter the rate: ")
try:
    
    hour = float(hour)
    rate = float(rate)
except:
    print("Opps! string input is not accepted")
    quit()
    
pay = hour*rate

print("Pay: ", pay)