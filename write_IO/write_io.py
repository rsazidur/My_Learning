# cities = ['Dhaka', 'Khulna', 'Barishal', 'Chittagong', 'Sylhet', 'Rangpur', 'Rajshahi']
#
# with open('cities.txt', 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)

# cities = []
#
# with open('cities.txt', 'r') as city_file:
#     for city in city_file:
#         cities.append(city)
# print(cities)
# for city in cities:
#     print(city, end="")

# imelda = "More Mayhem", "Imelda May", "2011", (
#          (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# with open("imelda.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)

with open('imelda.txt', 'r') as imelda_file:
    contents = imelda_file.readline()
imelda = eval(contents)

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
