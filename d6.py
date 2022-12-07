buffersteam = open("d6_input.txt").read()
letters = []

for x in range(14, len(buffersteam)):
    current_letter = buffersteam[x]
    if len(letters) < 13:
        letters.extend(buffersteam[:x])
    else:
        letters.clear()
        letters.extend(buffersteam[x-14:x])
    
    if all(letters.count(item) == 1 for item in letters):
        print(x)
