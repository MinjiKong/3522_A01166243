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
def calculator(user_input: int, param_one: int, param_two: int) -> None:
    operation_list = [calculate_hypotenuse, sum_function, subtract, multiply, divide]

    print(operation_list[user_input - 1](param_one, param_two))


if __name__ == "__main__":
    print("""
    1 to calculate hypotenuse
    2 to add
    3 to subtract
    4 to multiply
    5 to divide
    """)

    ui = int(input(""))

    v_one = int(input("enter first number: "))
    v_two = int(input("enter second number: "))

    calculator(ui, v_one, v_two)
