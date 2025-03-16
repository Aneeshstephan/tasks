
#1. Write a function safe_divide(a, b) that divides two numbers. If the denominator is zero, raise a ZeroDivisionError with the message "Cannot divide by zero".

def Safe_devide(a,b):   
    if b== 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a/b

try:
    a = int(input("Enter the numerator: "))
    b = int(input("Enter the denominator: "))
    result = Safe_devide(10, 2) 
    print(f"Result: {result}")
except ZeroDivisionError as e:
    print(f"Error: {e}")








