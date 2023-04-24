# inp = input("A give the word:\n")
# length = len(inp)
# print("There are ", length, " letters in the word.") 
# def is_correct():
    
#     inp1 = input("B enter the letter:\n")

#     for i in inp:
#         if inp1 in inp[0:(length-1)]:
        
#             print("Yeah! You got it!!")
        
#             break
     
# def is_wrong():
#     inp1 = input("B enter the letter:\n")

#     for i in inp:
#         if inp1 not in inp[0:(length-1)]:
#             print("Ups! One step down to death.😭🔪.")
#             inp1 = input("Another guess? ")

# is_correct()
# is_wrong()



def Hangman():
    word = "apple"
    tmp = "-"*len(word)
    print(tmp)
    word_try = 5

    while word_try>0:
        user_inp = input("Enter a letter\n")
        if user_inp in word:
            for i,w in enumerate(word):

                if w == user_inp:
                # if user_inp in word:
                    print("Yeah! You got it!!♥ CONGRATS")
                # w==user_inp
                    tmp = tmp[:i] + user_inp + tmp[i+1:]
                    print(tmp)
               
        # print(word.index())
        # word.replace( ,user_input, 1)
        else:
            print("Please guess another word")
            print(f'you have {word_try-1} try left')
            word_try -=1
        
        if tmp==word:
            print("Congrats")
            word_try = 0

Hangman()

    
        # word.replace(, new_char, )
        
        
        




             
        
        
            
        

