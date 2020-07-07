# for i in range(1,20):
#     print("i is now {}".format(i))

number = "9,325,547,968,787,253"
cleanedNumber= ""

# for i in range(0,len(number)):
#     if number[i] in "0123456789":
#         cleanedNumber= cleanedNumber + number[i]
# newnumber=int(cleanedNumber)
# print("THE NUMBER IS {}".format(newnumber))
for char in number:
    if char in "0123456789":
        cleanedNumber += char
newNumber=int(cleanedNumber)
print("THE NUMBER IS {}".format(newNumber))

for state in ("not pinin","no more","a stiff","bereft of life"):
    print("THE PARROT IS " + state)

for i in range(0,100,5):
    print("I IS {}".format(i))

for i in range(1,13):
    for j in range(1,11):
        print("{0} times {1} is {2}".format(i, j, i*j))
    #print("===================================")
    print('')