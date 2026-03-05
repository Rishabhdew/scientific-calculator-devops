import math
import logging

logging.basicConfig(filename='calculator.log', level=logging.INFO)

def square_root(x):
    result = math.sqrt(x)
    logging.info(f"sqrt({x}) = {result}")
    return result

def factorial(x):
    result = math.factorial(x)
    logging.info(f"factorial({x}) = {result}")
    return result

def natural_log(x):
    result = math.log(x)
    logging.info(f"ln({x}) = {result}")
    return result

def power(x, b):
    result = math.pow(x, b)
    logging.info(f"{x}^{b} = {result}")
    return result

while True:
    print("\nScientific Calculator")
    print("1. Square Root")
    print("2. Factorial")
    print("3. Natural Log")
    print("4. Power")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        x = float(input("Enter number: "))
        print(square_root(x))

    elif choice == 2:
        x = int(input("Enter number: "))
        print(factorial(x))

    elif choice == 3:
        x = float(input("Enter number: "))
        print(natural_log(x))

    elif choice == 4:
        x = float(input("Enter base: "))
        b = float(input("Enter power: "))
        print(power(x,b))

    else:
        break
