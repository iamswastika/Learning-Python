#Trying try except conditional structures

temp="5 degrees"
cel = 0
try:
    fahr=float(temp)
except:
    fahr=-1
fahr = 5.0
cel = (fahr-32.0)*5.0/9.0
print(cel)