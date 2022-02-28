names = input("Enter names: ")
name_list = names.split()

initials = ""
initials_list = []

for name in name_list:
    initials += name[0]

for i in range(0, len(initials),2):
    initials_list.append(initials[i:i + 2])
intitials_list = " ".join(initials_list)


print(intitials_list)

