#Write a program that prompts the user to input two numbers and display its HCF. The Highest Common Factor (HCF) also called the Greatest Common Divisor (GCD) of two whole numbers, is the largest whole number that’s a factor of both of them

num1, num2 =input("enter first number= "),input("enter second number= ")
if (num1.isdigit()== True and num2.isdigit()==True):
  def get_hcf(x,y):
      if x>y:
          min = y
      else:
          min = x
      for i in range(min,1, -1):
          if x%i == 0 and y%i == 0:
              return i
      return 1
  
  print("The HCF of %d and %d is %d" % (int(num1), int(num2), get_hcf(int(num1), int(num2))))
           
else:
  print("Please enter two whole numbers")
    
  
  
  
  

