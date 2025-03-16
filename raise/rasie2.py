#3. ⁠Write a function validate_marks(marks) that raises a ValueError if marks are less than 0 or greater than 100.
def Validate_marks(marks):
    if marks < 0 or marks > 100:
        raise ValueError("marks must be between 0 and 100.")
    print ("marks are valid.")

try:
    marks =int(input("enter a marks :"))
    Validate_marks(marks)
except ValueError as e:
    print("Error : {e}")