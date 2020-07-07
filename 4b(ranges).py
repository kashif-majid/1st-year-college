# my_list = list(range(0, 10))
# print(my_list)
#
# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
#
# print(even)
# print(odd)

# my_string = "abcdefghijklmnopqrstuvwxyz"
# print(my_string.index("e"))
# print(my_string[4])
#
# small_decimal = range(0, 10)
# print(small_decimal)
# print(small_decimal.index(3))
#
# odd = range(1, 10000, 2)
# print(odd)
# print(odd[987])
#
# sevens = range(7, 1000000, 7)
# x = int(input("please enter multiple of 7 less than one million:"))
# if x in sevens:
#     print("{} is divisble by 7".format(x))
#
# print(small_decimal)
# my_range = small_decimal[::2]
# print(my_range)
# print(my_range.index(4))

decimal = range(0, 100)
print(decimal)

my_range = decimal[3:40:3]
print(my_range)

for i in my_range:
    print(i)
print("=" * 40)

for i in range(3, 40, 3):
    print(i)

print(my_range==range(3, 40, 3))