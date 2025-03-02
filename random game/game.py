import random

system_number = random.randint(1, 10)
chances = 3

print("Guess the number!")
print("You have 3 chances to win.")

for attempt in range(chances):
    guess = int(input("Enter a number: "))
    
    if guess == system_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print(f"Wrong guess. You have  chances left.")

if guess != system_number:
    print("Sorry, you've used all your chances.")
    print(f"The correct number was {system_number}. Better luck next time!")
