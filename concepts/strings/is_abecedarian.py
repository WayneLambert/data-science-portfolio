"""
The following function returns True if the word passed as input is an
abecedarian word. That is a word where the each letter in the word is a
subsequent letter in the alphabet. 'Ant' would be a simple example.
"""


def is_string_abecederian(test_word: str) -> bool:
    max_letter = ''
    letters_tested = 0
    for letter in test_word.lower():
        if letter < max_letter:
            return False
        else:
            max_letter = letter
            letters_tested += 1
    if letters_tested == len(test_word):
        return True

""" Loop over each line in the file and test if the word is abecedarian. """

results = []
with open('concepts/strings/words.txt', 'r') as test_file:
    result = False
    for line in test_file:
        test_word = line.replace('\n', '')
        if is_string_abecederian(test_word):
            results.append(test_word)

print(f"There are {len(results)} abecedarian words in the file. These are:\n")
print(results)
