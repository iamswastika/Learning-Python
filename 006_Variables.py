#Variables are container to store a value
#In Python, a variable is created the moment you first assign a value to it

#Variable can be changed even after they have been set. The last one gets displayed. 

a= "Jake Peralta"
a= 'Jake Peralta'
a= '''"Jake Peralta"'''
a= '''Jake " ' Peralta'''
a= ''' Jake Peralta 
is a 
good
detective.''' 
b= 22
b= "Jake marries Amy." #Variable 'type' can be changed after they have been set
c= float(56.8) #Type Casting can be used to specify a datatype to a variable
C= 56.90887666605578379894302 #C won't overwrite c. C is a different variable. 
NineNineCaptain= "Captain Holt"
print(a)
print(type(b)) #To get datatype of a variable
print(c)
print(type(C))
print(NineNineCaptain)

#Variables with multiple values

Detective, Sergeant, Captain = "Jake", "Terry", "Holt"
print(Detective)
print(Sergeant)
print(Captain)
#OR
a, b, c = "Rosa", 20, 56.90 
print(a)
print(b)
print(c)

#Or
print(a, b, c)

#Multiple variables with one value

Detective=Sergeant=Captain = "Brooklyn Nine"
print(Detective)
print(Sergeant)
print(Captain)

#Unpacking the collection

Detectives= ["Jake", "Amy", "Charles", "Terry", "Rosa", "Hitchcock", "Scully"]
m, n, o, p, q, r, s = Detectives
print(m)
print(n)
print(o)
print(p)
print(q)
print(r)
print(s)

#Output in the same line

c1= "I"
c2= "Love"
c3= "Brooklyn Nine Nine"
print(c1, c2, c3)

#OR

c4= "I "
c5= "Love "
c6= "Brooklyn Nine Nine"
print(c4 + c5 + c6)


#In integers

c7= 8
c8 = 64
print(c7+c8)

#String and Integers

c9= 8
c10 = "Charles"
print(c9, c10)
#print(c9+ c10) -> unsupported operand

#Try
t = "Amy", 22, 60000
print(t)

t1 = ["Amy", 22, 60000]
print(t1)


#to define a floating point number, use one of the following notations
myfloat = 5.0
print(myfloat) 

myfloat = float(5) #Type Casting
print(myfloat)


#using double quotes makes it easy to include apostrophes

mystring = 'Hello learner!'
print(mystring)

myystring = "don't you dare give up!"
print(myystring)

# one = 1
# two = 2
# hello = "Hello"
# print(one + two + hello)  #won't work