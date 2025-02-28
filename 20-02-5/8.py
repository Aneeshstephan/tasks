def add(a, b):
    return "sum is", a + b

def sub(a, b):
    return "sub is", a - b

def mul(a, b):
    return "mul is", a * b

def div(a, b):
    return "div is", a / b

while True:
    choice = int(input("Enter operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit\n"))
    if choice in [1, 2, 3, 4]:
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        
        if choice == 1:
            print(add(x, y))
        elif choice == 2:
            print(sub(x, y))
        elif choice == 3:
            print(mul(x, y))
        elif choice == 4:
            print(div(x, y))
    elif choice == 5:
        print("Exiting the program")
        break
    else:
        print("Invalid choice. ")
