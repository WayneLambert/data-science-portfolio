# For Loops
for i in range(1, 201, 1):
    if i % 2 == 0:
        print(i)

# The above can be written as a succinct list comprehension
even_nums = [print(i) for i in range(1, 101) if i % 2 == 0]

# Similarly, odd numbers can be written with a small modification
odd_nums = [print(i) for i in range(1, 101) if i % 2 != 0]


num_vowels, num_consonants = 0, 0
test_string = "We wish you a merry Christmas and a happy new year"
for letter in test_string:
    if letter.lower() in 'aeiou':
        num_vowels += 1
    elif letter != " ":
        num_consonants += 1

print(f"{num_vowels} vowels and {num_consonants} consonants")


students = {
    "male": ["Tom", "Charlie", "Harry", "Frank"],
    "female": ["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
}

for key, value in students.items():
    for name in value:
        if "o" in name:
            print(name)
