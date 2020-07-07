# for i in range(10):
#     print("I IS NOW {}".format(i))
i = 0
# while i < 10:
#     print("I IS NOW {}".format(i))
#     i += 1
available_exit = ["east", "north east", "north"]
choosen_exit = ""
while choosen_exit not in available_exit:
    choosen_exit = input("CHOOSE YOUR DIRECTION:")
    if choosen_exit == "quit":
        print("game over")
        break
else:
    print("aren't you glad you came out")
