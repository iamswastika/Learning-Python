# Write a Python program to count the occurrences of each word in a given sentence.

from collections import Counter
def counting():
    inp = input("Say Something: ")
    counts=dict()
    words=inp.split()
    for word in words:
        counts[word] = counts.get(word,0)+1
    
    return Counter(words)

print(counting())







    