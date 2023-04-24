#a program to prompt a user for hours and rate per hour to compute gross pay

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
x=int(hours)
y=float(rate)
pay = x*y
# int*(rate)
print(f"Pay: {pay} ")
