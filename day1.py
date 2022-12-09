filename = 'day1_input.txt'
with open(filename) as f:
    content = f.read().splitlines()

class Elf:
    def __init__(self, number, calories):
        self.number = number
        self.calories = calories

elf_number = 0
elf = Elf(elf_number, 0)
elf_list = [elf]

calorie_total = []

for line in content:
    if line != "":
        elf_list[elf_number].calories += int(line)
        #print(elf_list[elf_number].calories)
    elif line == "":
        #print(elf_list[elf_number].calories)
        elf_number += 1
        elf_list.append(Elf(elf_number, 0))
        #print(elf_number)
    else:
        pass

for elf in range(len(elf_list)):
    calorie_total.append(elf_list[elf].calories)

calorie_total.sort(reverse = True)
print(calorie_total)

print(calorie_total[0] + calorie_total[1] + calorie_total[2])
