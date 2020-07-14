from functools import lru_cache

"""
The `lru_cache` function from the standard `functools` library as a decorator
to implement memoization (last result caching for re-use on next iteration)
"""
@lru_cache(maxsize=1000)
def fibonacci_recursive(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num > 1:
        return fibonacci_recursive(num - 1) + fibonacci_recursive(num - 2)


if __name__ == "__main__":
    for num in range(101):
        print(f"Fib {num} = {fibonacci_recursive(num)}")
