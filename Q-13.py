#13
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

user_input = input()
numbers = [int(x) for x in user_input.split()]

odd_total, even_total, odd_maximum, even_maximum, odd_minimum, even_minimum, odd_average, even_average = list_stats(numbers)

print("Sum (even):", even_total)
print("Sum (odd):", odd_total)
print("Max (even):", even_maximum)
print("Max (odd):", odd_maximum)
print("Min (even):", even_minimum)
print("Min (odd):", odd_minimum)
print("Avg (even):", even_average)
print("Avg (odd):", odd_average)

