"""
Calculates both the quotient and remainder of two arguments
"""

import math

# Uses the divmod function to return a tuple containing the quotient and remainder
div_mod_values = divmod(100, 12)
print(div_mod_values)

# Calculates just the quotient using standard Python arithmetic
quotient = 100 // 12
print(quotient)

# Calculates just the remainder using standard Python arithmetic
remainder = 100 % 12
print(remainder)

# Calculates the remainder (modulus) using the remainder function
# from the math module instead
remainder_from_math_module = math.remainder(100, 12)
print(remainder_from_math_module)
