#Write a Python program to get a string from a given string where all 
# occurrences of its first char have been changed to '$', except the first char itself.

stri=input("Enter a string: ")
first = stri[0]
c = ''
d=''
d += first
flag = 0
for i in stri:
    if i == first and flag == 0:
        c+=i
        flag = 1
    elif i == first and flag == 1:
        c += '$'
    else:
        c += i
for i in range(1,len(stri)):
    if stri[i] == first:
        d += '$'
    else:
        d += stri[i] 

print(d)
    
print(c)        
    


    