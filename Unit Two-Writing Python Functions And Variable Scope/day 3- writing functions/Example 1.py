import math

# arguments:
# function name:
# what does it return: 
def calculate_cylinder_volume(radius, height):
    return math.pi * radius**2 * height

def calculate_circle_area(radius):
    return math.pi * radius**2

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def convert_temperature(degrees, scale):
    if scale.lower() == 'celsius':
        fahrenheit = (degrees * 9/5) + 32
        return fahrenheit
    elif scale.lower() == 'fahrenheit':
        celsius = (degrees - 32) * 5/9
        return celsius
    else:
        return None

# 



####################################################
