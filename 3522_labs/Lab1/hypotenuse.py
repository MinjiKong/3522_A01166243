import math

"""
Return the length of a hypotenuse calculated between the two parameter numbers which represent the sides of a triangle.
:param a: an int or float representing side a.
:param b: an int or float representing side b.
:precondition: a must be an int or a float.
:precondition: b must be an int or a float.
:return: the length of the hypotenuse between the sides.
"""


def calculate_hypotenuse(a: int or float, b: int or float) -> float:
    return math.sqrt((a ** 2 + b ** 2))


"""
Return the sum of the two parameters.
:param a: an int or float to be summed.
:param b: an int or float to be summed.
:precondition: a must be an int or a float.
:precondition: b must be an int or a float.
:return: the sum of both parameters.
"""


def sum_function(a: int or float, b: int or float) -> int or float:
    return a + b


"""
Return the difference between the two parameters.
:param a: an int or float to find the difference of.
:param b: an int or float to find the difference of.
:precondition: a must be an int or a float.
:precondition: b must be an int or a float.
:return: the difference between both parameters.
"""


def subtract(a: int or float, b: int or float) -> int or float:
    return a - b


"""
Return the product between the two parameters.
:param a: an int or float to find the product of.
:param b: an int or float to find the product of.
:precondition: a must be an int or a float.
:precondition: b must be an int or a float.
:return: the product between both parameters.
"""


def multiply(a: int or float, b: int or float) -> int or float:
    return a * b


"""
Return the quotient between the two parameters.
:param a: an int or float to find the quotient of.
:param b: an int or float to find the quotient of.
:precondition: a must be an int or a float.
:precondition: b must be an int or a float.
:return: the quotient between both parameters.
"""


def divide(a: int or float, b: int or float) -> int or float:
    return a / b


"""
Return the value of the selected calculation.
:param user_input: an int or float that denotes the type of calculation.
:param param_one: the first parameter to be operated on.
:param param_two: the second parameter to be operated on.
:precondition: a must be an int or a float.
:precondition: a must be an int or a float.
:precondition: b must be an int or a float.
:return: the selected calculation between the inputted two parameters.
"""


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
