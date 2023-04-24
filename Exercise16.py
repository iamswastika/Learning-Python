#Write a Python program to calculate the length of a string. E.g “Apple” length in 5
def length(str):
    count=0
    for i in str:
        count=count+1
    print(count)
    
inp=input("Enter a string:")
length(inp)