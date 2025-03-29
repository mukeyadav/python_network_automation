def convert_number_to_binary_and_hex(number):
    try:
        # Convert the number to binary and hexadecimal
        binary = bin(number)
        hexadecimal = hex(number)

        # Return the results
        return {
            "binary": binary,
            "hexadecimal": hexadecimal
        }
    except TypeError:
        return "Invalid input. Please provide a valid number."

# Example usage
if __name__ == "__main__":
    try:
        # Get user input
        number = int(input("Enter a number: "))

        # Convert the number
        result = convert_number_to_binary_and_hex(number)

        # Display the results
        print(f"Number: {number}")
        print(f"Binary: {result['binary']}")
        print(f"Hexadecimal: {result['hexadecimal']}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
# This script converts a given number to its binary and hexadecimal representations.