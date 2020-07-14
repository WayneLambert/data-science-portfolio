"""
Prints a formatted list of the times tables
just like you learn at primary school
"""

end_with = 12

for i in range(1, end_with + 1):
    print(f"{str(i)} times table...")
    for j in range(1, end_with + 1):
        print(f"\t{i} {chr(215)} {j} = {i*j}")
