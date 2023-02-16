#2
nums = input("Enter two number: ").split()
num1= (nums[0])
num2= (nums[1])
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
  
  print( get_hcf(int(num1), int(num2)))
           
else:
  print("Please enter two whole numbers")
    
  
