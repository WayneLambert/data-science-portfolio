# These function check whether all of the elements being passed in are strings

# Method 1: List Comprehension
# All elements in list are strings, therefore evaluates to True
def is_all_strings(lst: list) -> bool:
    # sourcery skip: comprehension-to-generator
    return all([isinstance(element, str) for element in lst])

my_list = ['This', 'That', 'The Other']
print(f"{'All values in my_list are strings:'} {is_all_strings(my_list)}")


# Method 2: Generator Expression
# The 2 in the list is an integer, therefore evaluates to False
def is_all_strings(lst: list) -> bool:
    return all(isinstance(element, str) for element in lst)

my_list = ['This', 'That', 'The Other', 2]
print(f"{'All values in my_list are strings:'} {is_all_strings(my_list)}")
