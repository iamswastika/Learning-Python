file=open("File.txt")
# inp=file.read()
# print(inp)
# print(len(inp))

# # printing first 10 characters

# print(inp[:10])


for line in file:
    line =line.rstrip()
    if not line.startswith('H'): 
        continue
    print(line)
