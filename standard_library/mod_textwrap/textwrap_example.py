import textwrap

unformatted_str = '         This is a string to perform text wrapping operations on'

# Ordinary concatenation and left-stripping would achieve a bulleted item
bulleted = f"{'* '}{unformatted_str.lstrip()}"
print(bulleted)

# The same thing can be achieved using the textwrap module functions,
# although this version is less readable than the previous version
bulleted_indent = textwrap.indent(textwrap.dedent(unformatted_str), '* ')
print(bulleted_indent)


# Shortens the string to 15 characters and truncates to the nearest whole word
shortened_str = textwrap.shorten(bulleted_indent, 15, placeholder='...')
print(shortened_str)

# In this case, the shortened_str only needs to use 14 characters of the 15 to
# truncate the entire string to the nearest whole word
print(len(shortened_str))


# Wrap the original string (left-stripped) to characters
wrapped_text = textwrap.wrap(unformatted_str.lstrip(), 20)

# Prints list of wrapped text
print(wrapped_text)

# Iterate over the list to see each line individually
for wrappedline in wrapped_text:
    print(wrappedline)
