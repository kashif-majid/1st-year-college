# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# print(40 * "=")
#
# wild_animals = set(["tiger", "lion", "panther", "elephant"])
# print(wild_animals)
#
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)

# empty_set = {}
# empty_set_1 = set()
# empty_set_1.add("a")
#  empty_set.add("a")

# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# square_tuples = (4, 9, 16, 25)
# squares = set(square_tuples)
# print(squares)
# print(len(squares))
#
# print(even.union(squares))
# print(len(even.union(squares)))
# print(squares.union(even))
#
# print("=" * 40)
#
# print(even.intersection(squares))
# print(len(even & squares))
#
# print(squares & even)


# even = set(range(0, 40, 2))
# print(sorted(even))
#
# square_tuples = (4, 9, 16, 25)
# squares = set(square_tuples)
# print(sorted(squares))
#
# print("even minus squares")
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))
#
# print("squares minus even")
# print(sorted(squares.difference(even)))
# print(sorted(squares - even))
#
# print("=" * 40)
# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(sorted(even))
#
# print("=" * 40)
# print("symmetric even minus squares")
# print(sorted(even.symmetric_difference(squares)))
#
# print("symmetric squares minus even")
# print(sorted(squares.symmetric_difference(even)))

# even = set(range(0, 40, 2))
# print(even)
#
# square_tuples = (4, 9, 16, 25)
# squares = set(square_tuples)
# print(squares)

# squares.discard(4)
# squares.remove(16)
# squares.discard(8)
# print(squares)
#  if 8 in squares:
#      squares.remove(8)
# try:
#     squares.remove(8)
# except KeyError:
#     print("THIS SET DOESN'T CONTAIN 8")

# even = set(range(0, 40, 2))
# print(even)
#
# square_tuples = (4, 16)
# squares = set(square_tuples)
# print(squares)
#
# if squares.issubset(even):
#     print("squares is a subset of even")
# if even.issuperset(squares):
#     print("even is a superset of squares")
even = frozenset(range(0, 100, 2))
print(even)
# even.add(3)

