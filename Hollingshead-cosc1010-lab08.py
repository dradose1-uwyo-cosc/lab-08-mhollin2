# Margaret Hollingshead
# UWYO COSC 1010
# 11/7/24
# Lab 08
# Lab Section:18
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def string_convert(num):
    """This function converts an inputted string into an integer or a float to be used in calculations."""
    isNeg = False
    if num[0] == "-":
        num = num.replace("-","")
        isNeg = True
    if "." in num:
        num_list = num.split(".")
        if len(num_list) == 2 and num_list[0].isdigit() and num_list[1].isdigit():
            if isNeg:
                return -1 * float(num)
            else:
                return float(num)
    elif num.isdigit():
        if isNeg:
            return -1 * int(num)
        else:
            return int(num)
    else:
        return False

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, upper_x, lower_x):
    """This function calculates Y values in a give x boundary for a linear line."""
    Y_list = []
    length_x = upper_x - lower_x +1 
    value = 0
    while value < length_x:
        y = m*(lower_x + value) + b
        Y_list.append(y)
        value = value + 1
    return(Y_list)

input_list = []

while len(input_list) < 4:
    user_input = input("Please input the slope, intercept, upper x bound, and lower x bound:")
    input_list.append(user_input)
    if len(input_list) == 3:
        if "." in input_list[2]:
            print("Please input integers for the x bounds.")  
            break
    if len(input_list) == 4:
        if "." in input_list[3]:
            print("Please input integers for the x bounds.")
            break
    if "exit" in input_list:
        break

if len(input_list) == 4:
    slope = string_convert(input_list[0])
    intercept = string_convert(input_list[1])
    upper_x_bound = string_convert(input_list[2])
    lower_x_bound = string_convert(input_list[3])

    if upper_x_bound < lower_x_bound:
        print("The upper x bound must be larger than the lower x bound.")

result = slope_intercept(slope, intercept, upper_x_bound, lower_x_bound)
print(result)

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def Quadratic_formula(a,b,c):
    """This function uses the quadratic formula to calculate x intercepts."""
    y1 = (-b + (b**(2) - 4*a*c)**(1/2))/(2*a)
    y2 = (-b - (b**(2) - 4*a*c)**(1/2))/(2*a)
    return f"x={y1} and x={y2}"

quadratic_inputs = []

while len(quadratic_inputs) < 3:
    quad_user = input("Please input a, b, and c:")
    quadratic_inputs.append(quad_user)

if len(quadratic_inputs) == 3:
    a1 = string_convert(quadratic_inputs[0])
    b1 = string_convert(quadratic_inputs[1])
    c1 = string_convert(quadratic_inputs[2])

Quad_result = Quadratic_formula(a1,b1,c1)
print(Quad_result)
