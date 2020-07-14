# sourcery skip: collection-builtin-to-comprehension
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cubed_nums = (num ** 3 for num in nums)

# Iterate over the generator object
for cubed_num in cubed_nums:
    print(cubed_num)

# It could also have been cast as a list to return a single object
cubed_nums = list(num ** 3 for num in nums)

print(cubed_nums)
