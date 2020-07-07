shopping_item = ["egg", "juice", "spam", "bread", "milk", "fruits", "spam"]
for item in shopping_item:
    if item == "spam":
        print("I AM IGNORING " + item)
        continue
    print("BUY " + item)




meal = ["beans", "bacon", "egg", "spam"]
nasty_food_item = ""

for item in meal:
    if item == "spam":
        nasty_food_item = item
        break
else:
    print("I WOULD LIKE TO TAKE THE MEAL")
if nasty_food_item == "spam":
    print("I WOULD LIKE TO TAKE ANOTHER MEAL")

