# Write a Python script that takes input from the user and displays that
# input back in upper and lower cases.

# inp = input("Say Something: ")
# if(inp==inp.upper()):
#     print(inp.lower())
# else:
#     print(inp.upper())


def case_change(inp):
    z=""
    # c=""
    for i in inp:
        if ord(i)>=65 and ord(i)<=90:
            Y = ord(i)+32
            x=chr(Y)
            z=z+x
        elif ord(i)>=97 and ord(i)<=122:
            a= ord(i)-32
            b=chr(a)
            z=z+b
        else:
            z+=i 
    return z
   
print(case_change(input("Enter a string: ")))
    

    
    


