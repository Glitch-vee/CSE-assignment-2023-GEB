import numpy as np

user_input = input("Please enter a list of integers separated by spaces: ")
numbers = np.array([int(x) for x in user_input.split()])

# Using numpy's unique function to get unique values and the indices of their first occurrence
unique_values, indices, counts = np.unique(numbers, return_index=True, return_counts=True)

# Using numpy's where function to get the unique values that occurred only once
single_occurrence = unique_values[np.where(counts == 1)]

print("The integers which occurred only once in the list are:", single_occurrence)
ch