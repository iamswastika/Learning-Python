#counting words

fname=input('Enter File:')
if len(fname)<1 : 
    fname='demo.txt'
handle = open(fname)

di=dict()

for lin in handle:
    lin = lin.rstrip()
    # print(lin)
    
    wds = lin.split()
    # print(wds)
    
    for w in wds:
        #if not there, the count is zero
        # print('**', w, di.get(w,-99))
        # oldcount=di.get(w,0)
        # print(w,'old', oldcount)
        # newcount=oldcount+1
        # di[w]=newcount
        di[w]=di.get(w,0)+1
        # print(w, 'new', newcount)
        # print(w, 'new', di[w])
        
        # if w in di:
        #     di[w]=di[w]+1
        #     print('**Existing**')
        # else:
        #     di[w]=1
        #     print('**NEW**')
        # print(di[w])
# print(di)

#now we wanna find the most common word
largest=-1
for k,v in di.items():
    print(k,v)
    if v>largest:
        largest = v
        theword=k #capture/remember the word that was largest
    
print('Done', theword, largest)

# x = sorted(di.items()) #gives key-value pair
# print(x[:5])

tmp=list()
for k,v in di.items():
    print(k,v)
    newtuple = (v,k)
    tmp.append(newtuple)
    
# print('Flipped', tmp)

tmp = sorted(tmp, reverse = True)
# print('Sorted', tmp[:5])

for v, k in tmp[:5]:
    print(k,v)







    
    
    
    
    
    