def list_stats(numbers):
    total = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    average = total / len(numbers)
    return total, maximum, minimum, average

user_input = input("Please enter a list of integers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

total, maximum, minimum, average = list_stats(numbers)

print("The sum of the list is:", total)
print("The max of the list is:", maximum)
print("The min of the list is:", minimum)
print("The avg of the list is:", average)
