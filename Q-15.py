import random

# generating a random number
random_number = random.randint(1,100)

# initializing the number of tries
tries = 0

print("🎉 Welcome to the guessing game! 🎉")
print("🤔 Can you guess the secret number between 1 and 100? 🤔")

while True:
    guess = int(input("Make your guess: "))
    tries += 1
    if guess < random_number:
        print("🔻Too low, try again.🔻")
    elif guess > random_number:
        print("🔺Too high, try again.🔺")
    else:
        print("🎉 Congratulation, you have won the game in " + str(tries) + " tries! 🎉")
        if tries < 5:
            print("🏅 WOW! You are a pro at this! 🏅")
        elif tries < 10:
            print("🥇 Great job, you are a winner! 🥇")
        else:
            print("💪 Keep trying, you will get there! 💪")
        break
