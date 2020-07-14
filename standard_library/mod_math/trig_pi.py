"""
Calculates the sine, cosine, and tangent of various numbers
"""

import math

SIN_OF = 0.5
COS_OF = 90
TAN_OF = 1

sin_x = math.sin(SIN_OF * math.pi)
cos_x = math.cos(COS_OF * math.pi)
tan_x = math.tan(TAN_OF * math.pi)

print(f"""
Sine of {SIN_OF} {chr(215)} pi is {sin_x}
Cosine of {COS_OF} {chr(215)} pi is {cos_x}
Tangent of {TAN_OF} {chr(215)} pi is {tan_x}
""")
