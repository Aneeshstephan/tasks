#2. ⁠validate_password(password) that asserts the password must be at least 6 characters long.
def validate_password(password):
    assert len(password) >= 6, "The password must be at least 6 characters long!"
    print("password is valid.")

try:
    user_password = input("Enter your password:")
    validate_password(user_password)

except AssertionError as e:
    print(f"Error : e")