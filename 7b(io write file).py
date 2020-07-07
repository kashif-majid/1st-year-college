# cities = {"Sydney", "Srinagar", "Baramulla", "Melbourne"}
#
# with open("cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)

# cities = []
# with open("cities.txt", 'r') as city_file:
#     for city in city_file:
#         cities.append(city.strip("\n"))
# print(cities)
# for city in cities:
#     print(city)

# imelda = "MORE MAYHEM", "IMELDA MAY", "2011", (
#     (1, "PULLING THE RUG"), (2, "PSYCHO"), (3, "MAYHEM"),(4, "KENTISH TOWN WALTZ"))
#
# with open("imelda3.txt", "w") as imelda_file:
#     print(imelda, file=imelda_file)

with open("imelda3.txt", 'r') as imelda_file:
    content = imelda_file.readline()

imelda = eval(content)
print(imelda)
artist, title, year, tracks = imelda
print(artist)
print(title)
print(year)
print(tracks)