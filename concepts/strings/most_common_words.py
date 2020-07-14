""" Retrieves the most common words within the given text file. """


with open('concepts/strings/sample_text.txt', 'r') as file_to_check:
    # Count the frequency of the words
    counts = {}
    for line in file_to_check:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1

    # Find the most common word
    big_count = None
    big_word = None
    for word, count in counts.items():
        if big_count is None or count > big_count:
            big_word = word
            big_count = count

    print(f"The most common word is '{big_word}' which occurs {big_count} times.")
