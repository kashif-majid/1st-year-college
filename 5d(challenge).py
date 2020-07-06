locations = {0: "YOU ARE SEATING IN FRONT OF A COMPUTER LEARNING PYTHON",
             1: "YOU ARE STANDING AT THE END OF A ROAD BEFORE A SMALL BRICK BUILDING",
             2: "YOU ARE AT THE TOP OF A HILL",
             3: "YOU ARE INSIDE A BUILDING, A WELL HOUSE FOR A SMALL STREAM",
             4: "YOU ARE IN A VALLEY, BESIDE THE STREAM",
             5: "YOU ARE IN A FOREST"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

namedexits = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
              2: {"5": 5},
              3: {"1": 1},
              4: {"1": 1, "2": 2},
              5: {"2": 2, "1": 1}}

vocabulary = {"NORTH": "N",
              "WEST": "W",
              "SOUTH": "S",
              "EAST": "E",
              "QUIT": "Q",
              "ROAD": "1",
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5"}

# print(locations[0].split())
# print(locations[3].split(","))
# print(" ".join(locations[0].split()))

loc = 1
while True:
    availableexits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break
    else:
        allexits = exits[loc].copy()
        allexits.update(namedexits[loc])

    directions = input("AVAILABLE DIRECTIONS ARE " + availableexits + " :").upper()
    print()
    if len(directions) > 1:
        words = directions.split()
        for word in words:
            if word in vocabulary:
                directions = vocabulary[word]
                break

    if directions in allexits:
        loc = allexits[directions]
    else:
        print("YOU CANNOT GO IN THAT DIRECTION")
