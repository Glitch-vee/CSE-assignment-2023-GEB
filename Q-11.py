user_input = input("Please enter a string: ")
old_letter = input("Please enter the letter you want to replace: ")
new_letter = input("Please enter the letter you want to replace with: ")

new_string = user_input.replace(old_letter, new_letter)
print("The new string is:", new_string)
