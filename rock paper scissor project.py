import random  # import random module

print("Winning Rules of the Rock paper scissor game as follows: \n"
      + "Rock vs paper->Paper wins \n"
      + "Rock vs scissor->Rock wins \n"  # printing rules & instructions
      + "paper vs scissor->Scissor wins \n")
while True:
    print("Enter your choice \n 1 for Rock \n 2 for Paper \n 3 for Scissor \n")  # user's Choices
    choice = int(input("User turn:- "))  # User turn
    choice_name = 0

    while choice > 3 or choice < 1:  # Checking for valid input
        choice = int(input("Enter valid input:- "))

    if choice == 1:
        choice_name = 'Rock'  # Assigning values for user's input
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'

    print("User choice is: " + choice_name, "\n")
    print("\nNow its computer turn.......")
    comp_choice = random.randint(1, 3)
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissor'

    print("Computer choice is: " + comp_choice_name, "\n")

    print(choice_name + " V/s " + comp_choice_name, "\n")
    if ((choice == 1 and comp_choice == 2) or
            (choice == 2 and comp_choice == 1)):
        print("Paper wins => \n")
        result = "Paper"

    elif ((choice == 1 and comp_choice == 3) or
          (choice == 3 and comp_choice == 1)):
        print("Rock wins =>\n")
        result = "Rock"
    else:
        print("Scissor wins =>\n")
        result = "Scissor"

    if result == comp_choice_name:
        print("\t\t\t<== Computer wins!!! ==>\n")
    else:
        print("\t\t\t<== User wins!!! ==>\n")


    print("Do you want to play again? (Y/N)")
    Ans = input()
    if Ans == 'n' or Ans == 'N':
        print("\n\t\t\tThanks for playing:)")
        break




