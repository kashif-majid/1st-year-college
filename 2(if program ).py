name=input("ENTER YOUR NAME:")
age=int(input("ENTER YOUR AGE {}:".format(name)))
print(age)

if age >=18:
    print("ELIGIBLE TO VOTE")
    print("PLACE YOUR VOTE IN THE BALLOT")
else:
    print("COME BACK AFTER {} YEARS".format(18-age))