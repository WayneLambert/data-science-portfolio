import itertools

option_count = 0
for option in itertools.cycle((True, False)):
    option_count += 1
    if option_count > 10:
        break
    print(option)
