fruit = {"apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "orange": "a sweet, orange, citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
# print(fruit)
# print(fruit["lemon"])
# fruit["pear"] = "a odd shaped apple"
# print(fruit)
# fruit["lime"] = "great with tequila"
# print(fruit)
# del fruit["lemon"]
# print(fruit)
# fruit.clear()
print(fruit)
# while True:
#     dict_key = input("ENTER THE NAME OF FRUIT: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "WE DON'T HAVE A " + dict_key)
#     print(description)
#     # if dict_key in fruit:
#     #     description = fruit.get(dict_key)
#     #     print(description)
#     # else:
#     #     print("WE DON'T HAVE A" + dict_key)
# for i in fruit:
#     print(fruit[i])

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()

# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])

# for val in fruit.values():
#     print(val)

# for keys in fruit:
#     print(fruit[keys])

# print(fruit.keys())
#
# print(fruit.values())

# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)

print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snacks in f_tuple:
    item , description = snacks
    print(item + "is" + description)
print(dict(f_tuple))