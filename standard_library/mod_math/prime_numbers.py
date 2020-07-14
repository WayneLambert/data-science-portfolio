from time import time
from math import floor, sqrt

def is_prime(num: int) -> bool:
    """ Return `True` if `num` is a prime number, else `False` """
    if num == 1:
        return False  #1 is not prime

    # If it's even and not 2, then it's not prime
    if num == 2:
        return True
    if num > 2 and num % 2 == 0:
        return False

    max_divisor = floor(sqrt(num))
    return all(num % divisor != 0 for divisor in range(3, 1 + max_divisor, 2))

# ========= Time Function =========
start_time = time()
for num in range(1, 100_000):
    is_prime(num)
end_time = time()
print("Time required: ", end_time - start_time)
