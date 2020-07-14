from random import choice
# We can return functions from other functions


def make_laugh_func():
    def get_laugh():
        return choice(('HAHAHAH', 'lol', 'tehehe'))

    return get_laugh

laugh = make_laugh_func()
print(laugh())
