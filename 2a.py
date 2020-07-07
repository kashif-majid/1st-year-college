print("PLEASE GUESS A NUMBER BETWEEN 1 TO 10:")
guess=int(input())

if guess < 5:
    print("PLEASE GUESS HIGHER")
    guess=int(input())
    if guess == 5:
        print("WELL YOU HAVE GUESSED CORRECTLY")
    else:
        print("YOU GUESSED WRONG")
elif guess >5:
    print("PLEASE GUESS LOWER")
    guess=int(input())
    if guess ==5:
        print("WELL YOU GUESSED CORRECTLY")
    else:
        print("YOU GUESSED WRONG")
else:
    print("YOU GUESSED CPRRECTLY THE FIRST TIME")