#5. ⁠Write a function validate_email(email) that asserts the email must contain '@'.
def validate_email(email):
    assert "@" in email, "The email must contain '@'!"
    print("email is valid.")

try:
    user_email = input("Enter your email address: ")
    validate_email(user_email)

except AssertionError as e:
    print(f"error: e")