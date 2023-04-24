#  Write a Python program to count the number
# of characters (character frequency) in a string. Sample String : google.com' 
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1} 



def counting():
    inp = input("Enter a string: ")
    counts=dict()
    for word in inp:
        letters=word.split()
        for letter in letters:
            counts[letter]= counts.get(letter,0)+1
    return counts

print(counting())
   

    
        
      

    
    

    
