#12 
def list_stats(numbers):
    total = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    average = total / len(numbers)
    return total, maximum, minimum, average

user_input = input()
numbers = [int(x) for x in user_input.split()]

total, maximum, minimum, average = list_stats(numbers)

print("Sum:", total)
print("Max:", maximum)
print("Min:", minimum)
print("Avg:", average)
