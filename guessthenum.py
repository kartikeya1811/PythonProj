n = 15

for i in range(5):
    num = int(input("Guess the number: \n"))  # guess the number
    if num > n:  # number is less
        print("you guessed higher")
        print((4 - int(i)), "chance(s) remaining")
    elif num < n:  # number is more
        print("you guessed lower")
        print((4 - int(i)), "chance(s) remaining")
    else:
        print("You guessed right in",i+1,"guesses")
        break
print("Game over")
# chances left
