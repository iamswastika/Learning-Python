import random

CPU = random.randint(1, 100)


while True:
    userinput = int(input("Enter your guess: "))
    print(userinput)
    if(userinput>CPU):
        print("Guess Low")
    elif(userinput<CPU):
        print("Guess High")
    else:
        print("CONGRATULATIONS!!!")
        print("Yeah!!!")
        break


