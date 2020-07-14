def factorial(x):
    if x == 1:
        return 1
        # At this point, x is equal to 1, therefore the recursive call
        # under the else statement is not invoked.
        # The output of the function is returned
    else:
        return x * factorial(x - 1)
        # The function here calls itself again.
        # This line will not be executed once x == 1

print(factorial(5))

def fib(x):
    if x in [0, 1]:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)

print(fib(4))

def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)

print(power(2, 3))
