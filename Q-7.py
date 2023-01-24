#Write a program that asks the user for a positive integer value. The program should calculate the sum of all the integers from 1 up to the number entered. For example, if the user enters 20, the loop will find the sum of 1, 2, 3, 4, … 20.
#Input: 20 Output: 210


r = int(input("input the number range= "))

x=0

for i in range(1,r+1):
    x+=i
print("the sum of the numbers from 1 to ", r, 'is', x)   