#parsing, reading data

han = open('demo.txt')

for line in han:
    line = line.rstrip()
    print('Line:', line)
    
    # if len(wds)<1: #or 
    if line=='':
        print("Blank Line")
        continue
        # continue
    wds = line.split()
    print('Words:', wds)
    if wds[0]!='From':
        print('Ignore')
        continue
    print(wds[2])
    
    