# jabber = open("C:\\Users\\rsazi\\Desktop\\CSE111\\File.IO\\Read_IO\\Sample.txt", 'r')
#
# for line in jabber:
#     print(line)
# jabber.close()

# jabber = open("C:\\Users\\rsazi\\Desktop\\CSE111\\File.IO\\Read_IO\\Sample.txt", 'r')
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end="")
# jabber.close()

# with open("C:\\Users\\rsazi\\Desktop\\CSE111\\File.IO\\Read_IO\\Sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end="")


# with open("C:\\Users\\rsazi\\Desktop\\CSE111\\File.IO\\Read_IO\\Sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while True:
#         print(line, end="")
#         line = jabber.readline()

with open("C:\\Users\\rsazi\\Desktop\\CSE111\\File.IO\\Read_IO\\Sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines:
    print(line, end="")
