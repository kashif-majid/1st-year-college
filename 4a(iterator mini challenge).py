my_list = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
my_iterator = iter(my_list)
for i in range(0,len(my_list)):
    print(next(my_iterator))

for i in my_list:
    print(i)
