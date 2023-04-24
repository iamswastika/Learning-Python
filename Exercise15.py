#a program to read through a file and print the content of the file(line by line) all in upper case

inp = open(input("Enter a file: "))
for line in inp:
    line =line.rstrip()
    line = line.upper()
    print(line)
