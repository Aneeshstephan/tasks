
#2. ⁠Write a function check_password(password) that raises a ValueError if the password is less than 6 characters.

def Check_password(password):
    if len (password) < 6:
        raise ValueError("password must be at least 6 charactor long.")
    print("password is valid.")


try:
    password = input( "Enter your pasasword :")
    Check_password(password)
except ValueError as password:
    print("Error: {password}")