# #Variables that are created outside of a function are known as global variables.
# Can be used outside as well as inside a function
#Local variables are created inside the function and can be used inside the function only

#Program to create a variable outside of a function, and use it inside the function

x = "Happiness"

def myFunc():
    print(x, "is within us.")
    print("Everyone seeks " +x, ".")
    
myFunc()



#Concept of local and global variable together
#Program to create a variable inside a function, with the same name as the global variable

x = "Personality."

def globLoc():
    x = "Kindness."
    print("A person is defined by his " +x)
    
globLoc()

print("A person is defined by his " +x)

#Variable inside the function is local. 
#However, to make a variable inside a function a global variable, we use the global keyword.
#This variable can be used outside the function

def globVar():
    
    global y 
    y = "Sad."
    
globVar()

print("Do not be " +y, "Things are gonna be ok.")

    




