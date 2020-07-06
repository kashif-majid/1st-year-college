ip_address = input("PLEASE ENTER THE IP ADDRESS: ")
if ip_address[-1] != ".":
    ip_address += "."
segment = 1
segment_length = 0
# i = ""
for i in ip_address:
    if i == ".":
        print("segment {} contains {} character".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1

# if i != ".":
#     print("segment {} contains {} characters".format(segment, segment_length))










