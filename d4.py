inputpairs = open("d4_input.txt").read().splitlines()
numberofpairs = 0
firstelf, secondelf = zip(*(x.split(",") for x in inputpairs))
"""for x in range(len(firstelf)):
    first_start, first_end = firstelf[x].split("-")
    second_start, second_end = secondelf[x].split("-")
    
    if int(first_start) <= int(second_start) and int(first_end) >= int(second_end) or (int(first_start) >= int(second_start) and int(first_end) <= int(second_end)):
            numberofpairs += 1

print(numberofpairs)"""

for x in range(len(firstelf)):
    first_start, first_end = firstelf[x].split("-")
    first_range = range(int(first_start), int(first_end) + 1)
    second_start, second_end = secondelf[x].split("-")
    second_range = range(int(second_start), int(second_end) + 1)
    
    if len(list(set(first_range) & set(second_range))) > 0:
        numberofpairs += 1

print(numberofpairs)
