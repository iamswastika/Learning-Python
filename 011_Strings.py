#Multi-Line String

#three double quotes

a = """Python programming is fun.
It can be a good start for a programming career, 
as it is easy to learn."""
print(a)

#three single quotes

b = '''Python programming is fun.
It can be a good start for a programming career, 
as it is easy to learn.'''
print(a)

# Strings in Python are arrays of bytes representing unicode characters.

# ython does not have a character data type, a single character is simply a string with a length of 1.

# Square brackets can be used to access elements of the string.

#to get the character at position 1. position starts from 0

x = "Hello Programmer!"
print(x[1])

#Looping through strings

for p in "programmer":  #looping through each character/letters 
    print(p)   
    
#String Length

y = "hello! how are you?"
print(len(y))

# To check if a certain phrase or character is present in a string or not, we can use the keyword in

text = "old is gold"
print("old" in text)

#with if else
string = "health is wealth"
if("is" in string):
    print("the word is there")
else:
    print("ups! no word found")
    
#To check if certain phrase is not there in text with keyword not in

txt = " Everything is fair in love and war"
print("relation" not in txt)

#with if else

string1 = "brave and beautiful"
if("brown" not in string1):
    print("yeah it's not there")
else:
    print("there it is")
    
#Slicing Stringd
u="Hyy Ross "
print(u[2:5]) #gets characters from position 2 and position 4
print(u[:5]) #from beginning to position 5
print(u[2:])
print(u[-4:-1])
print(u.upper())
print(u.lower())
print(u.strip()) #removes any white spaces from the beginning or end
print(u.replace("y", "e"))

y = "Oh, My, God"
print(y.split(","))

#String Methods

# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Converts the elements of an iterable into a string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

#using format to insert number into string

age =22
moreage=25
Text= "I am {} years old. What did you think, I am {}."
print(Text.format(age, moreage)) 

ages =24
moreages=27
yourages=30
Texts= "I am {1} years old. What did you think, I am {2}. Your age is {0}"
print(Texts.format(yourages, ages, moreages)) 

txt= "we are fan of\" Friends.\"Are you?" #using double quotes inside string
print(txt)

#Escape Characters
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value
stuff= 'Hello World'
print(type(stuff))
print(dir(stuff))