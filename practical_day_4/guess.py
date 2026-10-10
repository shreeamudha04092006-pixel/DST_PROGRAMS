secret = 8
attempts = 0

while attempts < 5:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess < secret:
        print("Too Low")
    elif guess > secret:
        print("Too High")
    else:
        print("Correct")
        break

if attempts == 5 and guess != secret:
    print("Game Over")