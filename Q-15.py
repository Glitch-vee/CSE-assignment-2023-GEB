import random

# generating a random number
random_number = random.randint(1,100)

# initializing the number of tries
tries = 0

print("π Welcome to the guessing game! π")
print("π€ Can you guess the secret number between 1 and 100? π€")

while True:
    guess = int(input("Make your guess: "))
    tries += 1
    if guess < random_number:
        print("π»Too low, try again.π»")
    elif guess > random_number:
        print("πΊToo high, try again.πΊ")
    else:
        print("π Congratulation, you have won the game in " + str(tries) + " tries! π")
        if tries < 5:
            print("π WOW! You are a pro at this! π")
        elif tries < 10:
            print("π₯ Great job, you are a winner! π₯")
        else:
            print("πͺ Keep trying, you will get there! πͺ")
        break
