#1 
try:
 x=int(input("Enter number= ")) 
 print(bin(x)[2:],oct(x)[2:],hex(x)[2:], sep='\n')
except: 
 print("thats not an integer")
