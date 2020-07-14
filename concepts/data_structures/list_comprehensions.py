# List Comprehensions
# These are the combination of return values, for loops and [if statements]

# Build a list of even numbers from 1 - 100
# Method 2: stepped increase
even_nums = [num for num in range(1, 101) if num % 2 == 0]
print(even_nums)

# Build a list of even numbers from 1 - 100
# Method 2: stepped increase
even_nums = [num for num in range(0, 201, 2)]
print(even_nums)

# Build a list of odd numbers from 1 - 100
odd_nums = [num for num in range(1, 101) if num % 2 != 0]
print(odd_nums)

# Build a list of all even numbers from 0 - 100, raise them to the power of 3
# Method 1: modulo arithmetic
cubed_nums = [num ** 3 for num in range(101) if num % 2 == 0]
print(cubed_nums)

# Build a list of all even numbers from 0 - 100, raise them to the power of 3
# Method 2: stepped increase
cubed_nums = [num ** 3 for num in range(0, 101, 2)]
print(cubed_nums)

# Build a list of squared numbers from 1 - 200
squared_nums = [num ** 2 for num in range(201)]
print(squared_nums)

# Build a list called 'doubled_numbers' using standard iteration
doubled_numbers = [num * 2 for num in range(1, 11)]
print(doubled_numbers)

# Build a list called 'doubled_numbers' using a list comprehension
doubled_nums = [num * 2 for num in range(1, 11)]
print(doubled_nums)
