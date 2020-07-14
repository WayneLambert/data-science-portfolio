from fractions import Fraction

num = Fraction(6, 11)
den = Fraction(4, 5)


def add_frac(x, y):
    return x + y

print(add_frac(num, den))


def sub_frac(x, y):
    return x - y

print(sub_frac(num, den))


def mult_frac(x, y):
    return x * y

print(mult_frac(num, den))


def div_frac(x, y):
    return x / y

print(div_frac(num, den))


# As an illustration for adding improper fractions
num = Fraction(11, 6)
den = Fraction(5, 4)

print(add_frac(num, den))
