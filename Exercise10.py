#Displaying only those numbers from the list if:
#1. Numbers are divisible by five
#2. If the numbers are greater than 150, move to next number
#3. If the numbers are greater than 500, stop the loop

numbers=[12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i>500:
        break
    if i>150:
        continue
    if i%5==0:
        print(i)