print("PLEASE GUESS THE NUMBER BETWEEN 1 TO 10:")
guess=int(input())

if guess != 5:
    if guess < 5:
        print("PLEASE GUESS HIGHER")
    else:
        print("PLEASE GUESS LOWER")
    guess=int(input())
    if guess ==5:
        print("you guessed correctly")
    else:
        print("you guessed wrong")
else:
    print("YOU GUESSED CORRECTLY THE FIRST TIME")




