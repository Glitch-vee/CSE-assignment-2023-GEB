def list_stats(numbers):
    odd_numbers = [x for x in numbers if x % 2 != 0]
    even_numbers = [x for x in numbers if x % 2 == 0]
    odd_total = sum(odd_numbers)
    even_total = sum(even_numbers)
    odd_maximum = max(odd_numbers)
    even_maximum = max(even_numbers)
    odd_minimum = min(odd_numbers)
    even_minimum = min(even_numbers)
    odd_average = odd_total / len(odd_numbers)
    even_average = even_total / len(even_numbers)
    return odd_total, even_total, odd_maximum, even_maximum, odd_minimum, even_minimum, odd_average, even_average

user_input = input("Please enter a list of integers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

odd_total, even_total, odd_maximum, even_maximum, odd_minimum, even_minimum, odd_average, even_average = list_stats(numbers)

print("The sum of odd integers is:", odd_total)
print("The max of odd integers is:", odd_maximum)
print("The min of odd integers is:", odd_minimum)
print("The avg of odd integers is:", odd_average)

print("The sum of even integers is:", even_total)
print("The max of even integers is:", even_maximum)
print("The min of even integers is:", even_minimum)
print("The avg of even integers is:", even_average)
