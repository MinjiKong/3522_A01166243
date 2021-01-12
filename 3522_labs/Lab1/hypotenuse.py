import math


# Calculates the hypotenuse between two values
def calculate_hypotenuse(a: int or float, b: int or float) -> float:
    return math.sqrt((a ** 2 + b ** 2))


# Sums two values
def sum_function(a: int or float, b: int or float) -> int or float:
    return a + b


# Subtracts two values
def subtract(a: int or float, b: int or float) -> int or float:
    return a - b


# Multiplies two values
def multiply(a: int or float, b: int or float) -> int or float:
    return a * b


# Divides two values
def divide(a: int or float, b: int or float) -> int or float:
    return a / b


# Handles user inputs and calculates based on inputted values
def calculator():
    print("""
    1 to calculate hypotenuse
    2 to add
    3 to subtract
    4 to multiply
    5 to divide
    """)

    user_input = int(input(""))

    param_one = int(input("enter first number: "))
    param_two = int(input("enter second number: "))

    if user_input == 1:
        print(calculate_hypotenuse(param_one, param_two))
    elif user_input == 2:
        print(sum_function(param_one, param_two))
    elif user_input == 3:
        print(subtract(param_one, param_two))
    elif user_input == 4:
        print(multiply(param_one, param_two))
    elif user_input == 5:
        print(divide(param_one, param_two))
    else:
        print("Wrong value inputted")


if __name__ == "__main__":
    calculator()
