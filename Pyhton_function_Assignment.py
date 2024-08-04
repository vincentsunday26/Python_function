# Task 1: Define functions for each arithmetic operation
def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

# Task 2: Implement user input to receive numbers and an operation choice
def main():
    try:
        num_1 = float(input("Enter the first number: "))
        num_2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()

        # Task 3: Call the associated function based on user input and handle potential errors
        if operation == "add":
            result = add(num_1, num_2)
        elif operation == "subtract":
            result = subtract(num_1, num_2)
        elif operation == "multiply":
            result = multiply(num_1, num_2)
        elif operation == "divide":
            result = divide(num_1, num_2)
        else:
            result = "Error: Invalid operation."

        print(f"The result is: {result}")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()



# Assignment 2  The Shopping List Maker
# Function to add items to the list
def add_item(my_list):
    item = input("What would you like to add to the list? ")
    my_list.append(item)
    print(f"'{item}' has been added to the list.")

# Function to remove items from the list
def remove_item(my_list):
    item = input("What would you like to remove from the list? ")
    if item in my_list:
        my_list.remove(item)
        print(f"'{item}' has been removed from the list.")
    else:
        print(f"'{item}' is not in the list.")

# Function to print the entire list
def print_list(my_list):
    print("The current list is:")
    for item in my_list:
        print(f"- {item}")

# Main function to demonstrate the functionality
def main():
    my_list = []
    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Print list")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_item(my_list)
        elif choice == "2":
            remove_item(my_list)
        elif choice == "3":
            print_list(my_list)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
