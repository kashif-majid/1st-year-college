age= 24
print("my age is {0}".format(age))
print("thier  are {0} days in {1} {2} {3} {4} {5} {7}".format(31,"january" ,"march","may","july","august","october","december"))
print("""\njanuary:{2}
february:{0}
march:{2}
apri:{1}
may:{2}
june:{1}
july:{2}
august:{2}
september:{1}
october:{2}
november:{1}
december:{2}""".format(28,30,31))

print(" my age is %d years" % age)
print("my age is  %d %s %d %s" % (age, "years",  6, "months"))
for i in range(1,12):
    print("the no. %2d the square is %3d  the cube is %4d" %(i , i**2, i**3))

print("pie is approx. = %12.50f" %(22/7))

for i in range(1,12):
    print("the no. {0:2} the square is {1:3}  the cube is {2:4}".format(i , i**2, i**3))

print("pie is approx. = {0:12.50}" .format(22/7))

a="symb iosis"
print(a[::-1])