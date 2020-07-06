# imelda = "MORE MAHYEM", "EMILDA MAY", 2011,(
#         (1, "PULLING THE RUG"), (2, "PSYCHO"), (3, "MAHYEM"), (4,"KENTISH TOWN WALTZ" ))
#
# title, artist, year, tracks = imelda
# print(title,
#       artist,
#       year)
# for song in tracks:
#     track, title = song
#     print("\tTITLE NUMBER: {} , TITLE: {}:".format(track, title))


imelda = "MORE MAHYEM", "EMILDA MAY", 2011,(
        [(1, "PULLING THE RUG"), (2, "PSYCHO"), (3, "MAHYEM"), (4,"KENTISH TOWN WALTZ" )])
imelda[3].append((5,"ALL FOR YOU"))

title, artist, year, tracks = imelda
tracks.append((6,"ETERNITY"))
print(title,
      artist,
      year)
for song in tracks:
    track, title = song
    print("\tTITLE NUMBER: {} , TITLE: {}:".format(track, title))
