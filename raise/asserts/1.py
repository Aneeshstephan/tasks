#1. Write a function check_positive(num) that asserts the number must be greater than 0.
def check_positive(num):
    assert num > 0,  "The number must be greater than 0!"
    print(f"{num} is a positive number.")

try:
    number = float(input("enter a number : "))
    check_positive(number)
except AssertionError as e:
    print(f"Error : e")
except ValueError:
    print("Enter a valid number!")
