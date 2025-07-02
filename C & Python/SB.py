

import math

def custom_operation(value, char):
    if char == 'S':
        result = pow(2, value)
    elif char == 'B':
        result = math.sqrt(pow(value, 4))
    else:
        return "Invalid character!"
    
    return result

print(custom_operation(3, 'S'))
print(custom_operation(4, 'B'))
print(custom_operation(5, 'X'))