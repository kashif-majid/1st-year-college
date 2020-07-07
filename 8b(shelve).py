import shelve

# with shelve.open('ShelfTest') as fruit:
fruit = shelve.open('ShelfTest')
# fruit["apple"] = "good for making cider"
# fruit["lemon"] = "a sour, yellow citrus fruit"
# fruit["orange"] = "a sweet, orange, citrus fruit"
# fruit["grapes"] = "a small, sweet fruit growing in bunches"
# fruit["lime"] = "a sour, green citrus fruit"

# print(fruit["lemon"])
# print(fruit["orange"])
#
# fruit["lime"] = "great with tequila"
# for snack in fruit:
#     print(snack + ":" + fruit[snack])
# while True:
#     dict_key = input("Please Enter The Fruit: ")
#     if dict_key == "quit":
#         break
#     # if dict_key in fruit:
#     description = fruit.get(dict_key, "WE DON'T HAVE A " + dict_key)
#     print(description)
#     # else:
#     #     print("WE DON'T HAVE A " + dict_key)
# ordered_keys = list(fruit)
# ordered_keys.sort()
# for f in ordered_keys:
#     print(f +"-" + fruit[f])
for v in fruit.values():
    print(v)
print(fruit.values())

for i in fruit.items():
    print(i)
print(fruit.items())
fruit.close()
# print(fruit)