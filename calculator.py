import math

# ------ Calculator Functions -----

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def natural_log(x):
    return math.log(x)

def power(x, y):
    return x ** y


# ----- Interactive Menu -----

def run_calculator():
    print("Scientific Calculator")

    while True:
        print("\n1. Square Root")
        print("2. Factorial")
        print("3. Natural Log")
        print("4. Power")
        print("5. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            num = float(input("Enter number: "))
            print(square_root(num))

        elif choice == 2:
            num = int(input("Enter number: "))
            print(factorial(num))

        elif choice == 3:
            num = float(input("Enter number: "))
            print(natural_log(num))

        elif choice == 4:
            base = float(input("Enter base: "))
            exponent = float(input("Enter exponent: "))
            print(power(base, exponent))

        elif choice == 5:
            print("Exiting calculator...")
            break

        else:
            print("Invalid choice")


# ----------- Main Execution --------

if __name__ == "__main__":
    run_calculator()
