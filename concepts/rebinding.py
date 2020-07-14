# sourcery skip: while-to-for
"""
This is an example of rebinding. The integer of i upon each iteration is
actually a different object in Python's memory. This is demonstrated by the ID
being different upon each iteration. The integer, i, is being rebound each time.
"""

i = 1
ids = []
while i <= 5:
    ids.append(id(i))
    print(f"iteration {i} makes list become {ids}")
    i += 1
