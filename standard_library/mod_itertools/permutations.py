import itertools
from random import randint

letters = ('A', 'B', 'C', 'D', 'E')

# Returns 120 permutations since 5 letters means there are 5! permutations
print(len(list(itertools.permutations(letters))))

# Choose 6 lottery numbers at random
for _ in range(1, 7):
    num = [randint(1, 59)]
    if num in num:
        num = randint(1, 59)
    print(num)

my_permutations = list(itertools.permutations(letters, 5))
print(my_permutations)
