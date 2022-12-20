
file = open("1_1.txt", "r")
listOfCalories = []
elf = 0
a = "123456\n"

for line in file:
    if len(line) > 2:
        calories = int(line[0:-1])
        elf += calories

    else:
        listOfCalories.append(elf)
        elf = 0

for x in sorted(listOfCalories,reverse=True)[0:3]:
    elf += x
print(elf)

file.close
