locations = {0: {"desc": "YOU ARE SEATING IN FRONT OF A COMPUTER LEARNING PYTHON",
                 "exits": {},
                 "namedexits": {}},
             1: {"desc": "YOU ARE STANDING AT THE END OF A ROAD BEFORE A SMALL BRICK BUILDING",
                 "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                 "namedexits": {"2": 2, "3": 3, "5": 5, "4": 4}},
             2: {"desc": "YOU ARE AT THE TOP OF A HILL",
                 "exits": {"N": 5, "Q": 0},
                 "namedexits": {"5": 5}},
             3: {"desc": "YOU ARE INSIDE A BUILDING, A WELL HOUSE FOR A SMALL STREAM",
                 "exits": {"W": 1, "Q": 0},
                 "namedexits": {"1": 1}},
             4: {"desc": "YOU ARE IN A VALLEY, BESIDE THE STREAM",
                 "exits": {"N": 1, "W": 2, "Q": 0},
                 "namedexits": {"1": 1, "2": 2}},
             5: {"desc": "YOU ARE IN A FOREST",
                 "exits": {"W": 2, "S": 1, "Q": 0},
                 "namedexits": {"2": 2, "1": 1}}}


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


loc = 1
while True:
    availableexits = ", ".join(locations[loc]["exits"].keys())
    print(locations[loc]["desc"])

    if loc == 0:
        break
    else:
        allexits = locations[loc]["exits"].copy()
        allexits.update(locations[loc]["namedexits"])

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
