def computepay(hour, rate):
    y1=1.5*rate
    if(hour>40):
        bonuspay=(40*rate)+((hour-40)*y1)
        print(f"Pay: {bonuspay}")
    else:
        pay=hour*rate
        print("Pay: ", pay)
    

hour=input("Enter the hours: ")
x=float(hour)
rate=input("Enter the rate: ")
y=float(rate)
computepay(x,y)












# def computepay(hours, rate): 
#     bonuspay=(40*rate)+((x-40)+rate*1.5)
#     return bonuspay
    
# hours = float(input("Enter hours: "))
# rate = float(input("Enter rate: "))
# x =computepay(hours, rate)
# print(x)
