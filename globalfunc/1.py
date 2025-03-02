#1Modify a Global Variable Inside a Function
#Write a Python program where you define a global variable counter and create a function that increments its value by 1 each time it is called.

counter = 0
def increment_counter():
    global counter  
    counter += 1
    print(f"Counter value: {counter}")
increment_counter()
