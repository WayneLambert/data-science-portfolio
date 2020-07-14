"""
Lists the first n Fibonacci numbers using two different algorithms
1) List construction
2) Generator
"""


def fibonacci_numbers_list(previous=0, current=1, number=25):
    fib_nums = []
    for i in range(number):
        fib_nums.append(previous)
        print(f"fib {i} = {previous}")
        previous, current = current, previous + current
    return fib_nums


fibonacci_numbers_list(previous=0, current=1, number=51)


# An alternative function using a generator and a while loop
def fibonacci_numbers_generator(previous=0, current=1, number=101):
    # sourcery skip: while-to-for
    count = 0
    while count < number:
        previous, current = current, previous + current
        yield previous
        count += 1
        print(f"Fib {count} = {previous}")


"""
A loop that recursively calls the fibonnaci_numbers_generator function.
The `pass` function is merely there because the function requires it.
"""

for _ in fibonacci_numbers_generator(previous=0, current=1, number=101):
    pass
