# Python program to check whether the string is Symmetrical or Palindrome.Given a string.
# the task is to check if the string is symmetrical and palindrome or not. 
# A string is said to be symmetrical if both the halves of the string are 
# the same and a string is said to be a palindrome string if one half of the string is
# the reverse of the other half or if a string appears same when read forward or backward.

def is_palindrome(word):
    temp = ""
    for i in range(len(word)-1, -1, -1):
         temp = temp + word[i]
    if temp==word:
        return True
    else:
        return False
print(is_palindrome("amaama"))



def is_symmetrical(word):
    if len(word)%2==0:
        half = len(word)//2
        first_half = word[:half]
        second_half= word[half:]
        if first_half==second_half:
            print("It is Symmetrical")
        else:
            print("It is not Symmetrical")
    else:
        return False

print(is_symmetrical("hgjhtif"))

        
        
        
        
    
    



         
         
         