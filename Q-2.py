#1. Write a program that takes an integer value input and print its binary, octal and hexadecimal value as output

try:
    x=int(input("Enter number= "))
    print(bin(x),oct(x),hex(x), sep='\n')
except:
    print("thats not an integer")