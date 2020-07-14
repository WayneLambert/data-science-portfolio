def generate_evens1():
    return [number for number in range(2, 52, 2)]

list_evens = generate_evens1()
print(f"Genate Evens 1 Function: {list_evens}")


# The function itself can also be written as a list comprehension.
def generate_evens2():
    return [x for x in range(2, 52, 2)]

list_evens = generate_evens2()
print(f"Evens 2 Function: {list_evens}")


# Another variant of the function can be written using modulo arithmetic.
def generate_evens3():
    return [number for number in range(2, 52, 2) if number % 2 == 0]

list_evens = generate_evens3()
print(f"Evens 3 Function: {list_evens}")
