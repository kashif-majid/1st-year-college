# ipaddress = input("ENTER THE IP ADDRESS:")
# print(ipaddress.count("."))

# parrot_list = ["no more", "non pinin", "a stiff", "bereft of live"]
# parrot_list.append("a norweginin blue")
# for state in parrot_list:
#     print("THE PARROT IS " + state)
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
# number = even + odd
# numbers_is_sorted = sorted(number)
# # number.sort()
# print(numbers_is_sorted)
#
# if numbers_is_sorted == number:
#     print("THEY ARE EQUAL")
# else:
#     print("THEY ARE NOT EQUAL")
#
# if numbers_is_sorted == sorted(number):
#     print("THEY ARE EQUAL")
# else:
#     print("THEY ARE NOT EQUAL")

# list_1 = []
# list_2 = list()
#
# print("LIST 1: {}".format(list_1))
# print("LIST 2: {}".format(list_2))
#
# if list_1 == list_2:
#     print("THEY ARE EQUAL")
# print(list("THEY ARE EQUAL"))
# even = [2, 4, 6, 8]
# another_even = sorted(even, reverse=True)
# print(another_even == even)
# another_even.sort(reverse=True)
# print(even)
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = [even, odd]
# print(numbers)
for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value)



