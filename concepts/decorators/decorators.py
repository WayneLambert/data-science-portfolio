def surround_with(surrounding):
    """Return a function that takes a single argument and surrounds it."""
    def surround_with_value(word):
        return f'{surrounding}{word}{surrounding}'
    return surround_with_value


def transform_words(content, targets, transform):
    """Return a string based on *content* but with each occurrence of words in
        *targets* replaced with the result of applying *transform* to it."""
    result = ''
    for word in content.split():
        result += f'{transform(word)}' if word in targets else f'{word}'
        return result


markdown_string = """My name is Wayne Lambert and I like football but I do
                    not own a football"""
markdown_string_italicized = transform_words(markdown_string, ['football',
                                             'Wayne'], surround_with('*'))
print(markdown_string_italicized)
