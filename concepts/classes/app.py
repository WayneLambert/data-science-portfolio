class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f"""Tried to add a '{car.__class.__name}' to the
                garage, but you can only add 'car' objects.""")
        raise NotImplementedError("We cannot add cars to the garage yet.")


ford = Garage()
ford.add_car('Fiesta')
print(len(ford))

try:
    ford.add_car('Fiesta')
except TypeError:
    print('Your car was not a car!')
