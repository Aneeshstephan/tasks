#1. Write a program to read a file. Handle the exception if the file does not exist.


try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print("File content:")
        print(content)

except FileNotFoundError:
    print("Error: The file does not exist. Please check the file name and try again.")



#2. ⁠Write a program that takes an index from the user and prints the element from a predefined list. 
# Handle the case when the user enters an out-of-range index.

my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
try:
    index = int(input("Enter the index of the element you want to access: "))
    
    element = my_list[index]
    print(f"The element at index {index} is: {element}")

except IndexError:
    print("Error: The index you entered is out of range. Please try again with a valid index.")
except ValueError:
    print("Error: Please enter a valid integer index.")


#3 . ⁠Write a program to get a value from a dictionary by asking the user for a key. Handle the case when the key does not exist

sample_dict = {
    "name": "Aneesh",
    "age": 25,
    "location": "Kerala",
    "profession": "Developer"
}

key = input("Enter the key to retrieve the value: ")

try:
    value = sample_dict[key]
    print(f"The value for '{key}' is: {value}")
except KeyError:
    print(f"Error: The key '{key}' does not exist in the dictionary.")

#4. ⁠Write a program to take two numbers from the user and divide them. Handle zero division, invalid input, and unexpected errors.

def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = num1 / num2
        print(f"The result of dividing {num1} by {num2} is: {result}")
    
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    
    except ValueError:
        print("Error: Please enter valid numeric values.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

divide_numbers()
