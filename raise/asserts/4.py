#4. ⁠Write a function check_voting_eligibility(age) that asserts the person must be 18 or older.
def check_voting_eligibility(age):
    assert age > 18, "The age must be greater than 18!"
    print("You are eligible to vote.")

try:
    age = int(input("Enter the age:"))
    check_voting_eligibility(age)
except AssertionError as e:
    print(f"Error: e")
except ValueError:
    print("Please enter a eligeble age!")