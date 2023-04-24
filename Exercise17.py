# Write a Python program to get a string made of the first 2 and last 2
# characters of a given string. If the string length is less than 2, return the
# empty string instead.


def getstring():
    inp=input("Enter a string: ")
    j=inp[:2]
    i=inp[-2:]
    z=j+i
    if(len(j)<2):
        print("Empty String")
    else:
        print(z)
        
getstring()
    




