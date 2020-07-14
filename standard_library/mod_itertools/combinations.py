import itertools
from random import randint

letters = ('A', 'B', 'C', 'D', 'E')

# Choose 6 lottery numbers at random
for _ in range(1, 7):
    num = [randint(1, 59)]
    if num in num:
        num = randint(1, 59)
    print(num)

my_combinations = list(itertools.combinations(letters, 5))
print(my_combinations)
