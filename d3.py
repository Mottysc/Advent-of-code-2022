rucksacks = open("d3_input.txt").read().splitlines()
#ord(letter)-96
#ord(upperc)-38
letters = []
"""
for sack in rucksacks:
    sack_list = list(sack)
    midpoint = int(len(sack_list) / 2)
    for letter in sack_list[:midpoint]:
        if letter in sack_list[midpoint:]:
            letters.append(letter)
            break

print(letters)
letter_total = 0
for letter in letters:
    if letter.isupper():
        letter_total += int(ord(letter) - 38)
    else:
        letter_total += int(ord(letter) - 96)
        
print(letter_total)"""

for x in range(0, len(rucksacks), 3):
    sack_list = [list(rucksacks[x]), list(rucksacks[x + 1]), list(rucksacks[x + 2])]
    for letter in sack_list[0]:
        if letter in sack_list[1] and letter in sack_list[2]:
            letters.append(letter)
            break
        
print(letters)
letter_total = 0
for letter in letters:
    if letter.isupper():
        letter_total += int(ord(letter) - 38)
    else:
        letter_total += int(ord(letter) - 96)
        
print(letter_total)
print(len(letters))
