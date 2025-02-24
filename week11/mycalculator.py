def calculator():
    """
    A simple calculator application.
    """
    print("Welcome to the Calculator Application!")
    while True:
        choice = display_menu()
        if choice == 5:  # Exit option
            print("Thank you for using the calculator. Goodbye!")
            break
        result = handle_choice(choice)
        if result is not None:
            print(f"Result: {result}")


def display_menu():
    """
    Displays the menu and gets the user's choice.
    """
    print("\nPlease select the operation you want to perform:")
    print("1. Factorial")
    print("2. Prime Check")
    print("3. Power")
    print("4. Exit")

    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Error: Invalid choice. Please try again.")
        except ValueError:
            print("Error: Invalid input. Please try again.")


def handle_choice(choice):
    """
    Handles the user's choice and performs the corresponding operation.
    """
    if choice == 1:
        return perform_factorial()
    elif choice == 2:
        return perform_prime_check()
    elif choice == 3:
        return perform_power()


def perform_factorial():
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("Error: Factorial can only be calculated for non-negative integers.")
        return None
    return factorial(n)


def perform_prime_check():
    n = int(input("Enter an integer: "))
    return is_prime(n)


def perform_power():
    base = float(input("Enter the base: "))
    exponent = float(input("Enter the exponent: "))
    return power(base, exponent)


def power(base, exponent):
    return base ** exponent


def factorial(n):
    """
    Calculates the factorial of a given integer.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def is_prime(n):
    """
    Checks if a given integer is a prime number.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    calculator()
