from decimal import Decimal
import datetime


class Employee:
    num_of_employees = 0   # This is a class variable
    RAISE_AMOUNT = 1.08    # This is a class constant

    def __init__(self, first, last, pay):
        self.first = first     # This is an instance variable
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@domain.com".lower()
        Employee.num_of_employees += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * Employee.RAISE_AMOUNT)

    # Example of the fullname function as a property by using a decorator
    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    # Example of a setter property so that the full name can be set
    # Note difference of spelling for full_name - differentiates between
    # previously defined function called fullname
    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    """ An example of a class method. Notice the @classmethod decorator and the
        'cls' argument being used to denote that it's a class rather than 'self'
        which would denote that it is an instance of the class."""
    @classmethod
    def apply_raise_class_method(cls, amount):
        cls.RAISE_AMOUNT = amount

    # The @classmethod decorator here is being used as an alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        return not 5 <= day.weekday() <= 6


print(f'Number of Employees before contructing an instance of the employee class: \
{Employee.num_of_employees}')

# Two examples using ordinal arguments
emp_1 = Employee('Wayne', 'Lambert', 375 * 223)
emp_2 = Employee('Tom', 'Jones', 50000.43)

# An example using named parameters
emp_3 = Employee(last='Smith', first='Johnny', pay=40000)

print(f'Number of Employees after contructing an instance of the employee class: \
{Employee.num_of_employees}')

print(emp_1.email)
print(emp_2.email)
print(emp_3.email)
print(bn.format_currency(round(emp_1.pay, 0), "GBP"))
print(emp_1.fullname())

# Check to see if a date if a weekday...
date_to_check = Employee.is_workday(datetime.date(2019, 2, 4))
print(date_to_check)

# Checks pay before pay rise
print(f"Employee 1's pay before is {bn.format_currency(round(emp_1.pay,0), 'GBP')}")
emp_1.apply_raise()

# Checks the new amount once the pay rise has been applied
print(f"Employee 1's pay after the pay rise is \
{bn.format_currency(round(emp_1.pay,0), 'GBP')}")
print(emp_1.__dict__)


# An example of inheritance
# Creating a class called 'Developer' based upon its parent class 'Employee'
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)


dev_1 = Developer('Wayne', 'Lambert', 100000, 'Python')
dev_2 = Developer('Corey', 'Schafer', 50000, 'Java')

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

# Check to see if a class is a sub class of another

# True - Developer is a subclass of Employee
print(issubclass(Developer, Employee))

# False - Developer is not a instance of Employee
print(isinstance(Developer, Employee))

# True - emp_1 is an instance of Employee
print(isinstance(emp_1, Employee))
