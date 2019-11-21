from random import choice
from time import perf_counter

names = ['Wayne', 'Barrie', 'Rachael', 'Carrie']
majors = ['Programming', 'Lorry driving', 'Secretary', 'Bank Manager']


def people_list(num_people: int) -> list:
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': choice(names),
            'major': choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people: int):
    for i in range(num_people):
        person = {
            'id': i,
            'name': choice(names),
            'majors': choice((majors))
        }
        yield person


t1 = perf_counter()
people = people_list(1000000)
t2 = perf_counter()
print(people)

t1 = perf_counter()
people = people_generator(1000000)
t2 = perf_counter()
print(people)

# Prints the time taken
print(f'Taken: {t2 - t1}')
