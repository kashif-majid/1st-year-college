import pickle
# imelda = ("MORE MAYHEM",
#           "IMELDA MAY",
#           "2011",
#           ((1, "PULLING THE RUG"),
#            (2, "PSYCHO"),
#            (3, "MAYHEM"),
#            (4, "KENTISH TOWN WALTZ")))
#
# with open("imelda.pickle", 'wb') as pickle_file:
#     pickle.dump(imelda, pickle_file)


# with open("imelda.pickle", 'rb') as imelda_pickled:
#     imelda2 = pickle.load(imelda_pickled)
#
# print(imelda2)
#
# album, artist, year, track_list = imelda2
# print(album)
# print(artist)
# print(year)
# for track in track_list:
#     track_number, track_title = track
#     print(track_number, track_title)



imelda = ("MORE MAYHEM",
          "IMELDA MAY",
          "2011",
          ((1, "PULLING THE RUG"),
           (2, "PSYCHO"),
           (3, "MAYHEM"),
           (4, "KENTISH TOWN WALTZ")))

even = list(range(0, 10, 2))
odd = list(range(0, 10, 2))

with open("imelda.pickle", 'wb') as pickle_file:
    pickle.dump(imelda, pickle_file)
    pickle.dump(even, pickle_file)
    pickle.dump(odd, pickle_file)
    pickle.dump(33232, pickle_file)

with open("imelda.pickle", 'rb') as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)
    even_list = pickle.load(imelda_pickled)
    odd_list = pickle.load(imelda_pickled)
    x = pickle.load(imelda_pickled)


print(imelda2)

album, artist, year, track_list = imelda2
print(album)
print(artist)
print(year)
for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)

print("=" * 40)

for i in even_list:
    print(i)

print("=" * 40)

for i in odd_list:
    print(i)

print("=" * 40)
print(x)

# pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR.") #deletes the file