with open("d1_input.txt") as f:
    inputstring = f.read()
elveslist = inputstring.split("\n\n")
newelves = []
for elf in elveslist:
    splitelves = elf.split("\n")
    listelves = []
    for cals in splitelves:
        cals = int(cals)
        listelves.append(cals)
    newelves.append(listelves)

sumofcals = []
for elf in newelves:
    sumofcals.append(sum(elf))

sumofcals.sort(reverse=True)
print(sum(sumofcals[0:3]))