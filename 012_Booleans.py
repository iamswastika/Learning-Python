print(10>9)
print(9>10)
print(9==10)

a=88
b=97

if(a>b):
    print("greater")
else:
    print("smaller")
    
print(bool("Hello"))
print(bool(4))  

c="Hy"

print(bool(a))
print(bool(c))  

# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.

print(bool(2))
print(bool("Hello"))
print(bool(["Ross", 1, 9,9]))

print(bool(None))
print(bool(False))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(0))

class myclass():
    def __len__(self):
        return 0
    
myobj = myclass()
print(bool(myobj))

#function returning booloean

def myFunction():
    return True
print(myFunction())

def myFunction():
    return True
if myFunction():
    print("Yes")
else:
    print("No")

x=100
print(isinstance(x, float)) #isinstance() is a built-in function that returns a boolean value; determines if an object is of certain datatype