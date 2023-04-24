#Program to find the portion of the string after colon using find() function and string slicing. 
#The given string is str = 'X-DSPAM-Confidence: 0.8475'

# str = 'X-DSPAM-Confidence: 0.8475'
# i= str.find("0")
# print(i)
# j =str[19:26]
# print(float(j))

str = 'X-DSPAM-Confidence: 0.8475'
i = str.find(":")
j=str[i+2:]
print(float(j)) 