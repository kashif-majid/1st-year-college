locations = {0: "YOU ARE SEATING IN FRONT OF A COMPUTER LEARNING PYTHON",
             1: "YOU ARE STANDING AT THE END OF A ROAD BEFORE A SMALL BRICK BUILDING",
             2: "YOU ARE AT THE TOP OF A HILL",
             3: "YOU ARE INSIDE A BUILDING, A WELL HOUSE FOR A SMALL STREAM",
             4: "YOU ARE IN A VALLEY, BESIDE THE STREAM",
             5: "YOU ARE IN A FOREST"}

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S":4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]

loc = 1
while True:
    availableexits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break

    directions = input("AVAILABLE DIRECTIONS ARE " + availableexits + " :").upper()
    print()
    if directions in exits[loc]:
        loc = exits[loc][directions]
    else:
        print("YOU CANNOT GO IN THAT DIRECTION")
