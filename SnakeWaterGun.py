import random

obj = ["snake", "water", "gun"]

k = 0
yourscr = 0
compscr = 0

while k <= 10:
    print("\nchoose", end=" ")
    for i in obj:
        print(i, end=" ")
    print("as s,w,g")

    a = input()
    b = random.choice(obj)
    print(f"Computer chose {b} ")
    sett = {a, b}

    if sett == {"water", "s"}:
        print("snake ne water pi liya, You win")
        yourscr = yourscr + 1
    elif sett == {"w", "snake"}:
        print("snake ne water pi liya, computer wins")
        compscr = compscr + 1
    elif sett == {"w", "gun"}:
        print("water mein gun doob gayi, You win")
        yourscr = yourscr + 1
    elif sett == {"water", "g"}:
        print("water mein gun doob gayi, Comp wins")
        compscr = compscr + 1
    elif sett == {"g", "snake"}:
        print("gun ne snake ko maar diya, You win")
        yourscr = yourscr + 1
    elif sett == {"gun", "s"}:
        print("gun ne snake ko maar diya, Computer wins")
        compscr = compscr + 1
    elif sett == {"water", "w"} or sett == {"gun", "g"} or sett == {"snake", "s"}:
        print("Its a draw!!")
    else:
        print("Invalid input :P")
        k = k - 1
    k = k + 1
    continue
if yourscr > compscr:
    print("You won the game with", yourscr, "points")
    print("Computer score is ", compscr)
else:
    print("Computer won the game with", compscr, "points")
    print("Your score is ", yourscr)
