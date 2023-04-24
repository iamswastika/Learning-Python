#Rewrite the pay computation to give the employee 1.5 time the hourly rate for hours worked above 40 hours

hour=input("Enter the hours: ")
x=float(hour)
rate=input("Enter the rate: ")
y=float(rate)
y1=1.5*y
if(x>40):
    bonuspay=(40*y)+((x-40)*y1)
    print(f"Pay: {bonuspay}")
else:
   pay=x*y
   print("Pay: ", pay)
