#Guess the number
import random
target=random.randint(1,100)
attempt=5
print("Welcome to guess the number game")
print(f"You have {attempt} chances to guess the number range between 1 and 100")
for i in range(1,attempt+1):
    guess=int(input("Enter the number:"))
    if guess==target:
        print("Congratulations You are Won! :)")
        break
    elif guess<target:
        print("You too low,Try again")
    else:
        print("You too high,Try again")
else:
    print("Sorry you're out of attempt,the correct number was:{}".format(target))
