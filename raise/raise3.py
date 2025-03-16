# ⁠Write a function withdraw(amount, balance) that raises a RuntimeError if the withdrawal amount is greater than the balance.
def Withdraw(amount,balance):
    if amount > balance:
        raise RuntimeError ("withdrawal amount exceeds the avilable balance.")
    balance -=amount
    print(f"withdrawal seccessfull. remaining balance: {balance}")
    return balance

try:
    balance=float(input("enter your account balance :"))
    amount = float(input("Enter the amount to withdra:"))
    balance = Withdraw(amount , balance)
except RuntimeError as e:
    print(f"error: {e}")
except ValueError:
    print("please enter a valid number")