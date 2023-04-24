#Counting total numbers of digits in a number using while loop

x = str(input("Enter a digit: "))
counter=0
while x[counter:]:
    counter=counter+1

print(counter)
