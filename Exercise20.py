# Write a Python function that takes a list of words and return the longest
# word and the length of the longest one.

def fun():
    listt=["apple", "banana", "orthodontist", "bag"]
    x = len(listt[0])
    longest = listt[0]
    for i in listt:
        if len(i) > x:
            x=len(i)
            longest = i
        else:
            continue

    print(longest)
    count=0
    for i in longest:
        count=count+1
    print(count)
fun()

    

    



