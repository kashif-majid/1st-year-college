import shelve
locations = shelve.open("locations")
vocabulary = shelve.open("vocabulary")
loc = "1"
while True:
    availableexits = ", ".join(locations[loc]["exits"].keys())
    print(locations[loc]["desc"])

    if loc == "0":
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
locations.close()
vocabulary.close()