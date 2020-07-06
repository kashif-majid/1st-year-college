import shelve
locations = shelve.open("locations")
locations["0"] = {"desc": "YOU ARE SEATING IN FRONT OF A COMPUTER LEARNING PYTHON",
                  "exits": {},
                  "namedexits": {}}
locations["1"] = {"desc": "YOU ARE STANDING AT THE END OF A ROAD BEFORE A SMALL BRICK BUILDING",
                  "exits": {"W": "2", "E": "3", "N": "5", "S": "4", "Q": "0"},
                  "namedexits": {"2": "2", "3": "3", "5": "5", "4": "4"}}
locations["2"] = {"desc": "YOU ARE AT THE TOP OF A HILL",
                  "exits": {"N": "5", "Q": "0"},
                  "namedexits": {"5": "5"}}
locations["3"] = {"desc": "YOU ARE INSIDE A BUILDING, A WELL HOUSE FOR A SMALL STREAM",
                  "exits": {"W": "1", "Q": "0"},
                  "namedexits": {"1": "1"}}
locations["4"] = {"desc": "YOU ARE IN A VALLEY, BESIDE THE STREAM",
                  "exits": {"N": "1", "W": "2", "Q": "0"},
                  "namedexits": {"1": "1", "2": "2"}}
locations["5"] = {"desc": "YOU ARE IN A FOREST",
                  "exits": {"W": "2", "S": "1", "Q": "0"},
                  "namedexits": {"2": "2", "1": "1"}}
locations.close()
vocabulary = shelve.open("vocabulary")
vocabulary["NORTH"] = "N"
vocabulary["WEST"] = "W"
vocabulary["SOUTH"] = "S"
vocabulary["EAST"] = "E"
vocabulary["QUIT"] = "Q"
vocabulary["ROAD"] = "1"
vocabulary["HILL"] = "2"
vocabulary["BUILDING"] = "3"
vocabulary["VALLEY"] = "4"
vocabulary["FOREST"] = "5"

vocabulary.close()
