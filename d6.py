buffersteam = open("d6_input.txt").read()

for x in range(4, len(buffersteam)-4):
    letters = []
    letters.extend(buffersteam[x-3:x])
    if buffersteam[x] in letters:
        pass
    else:
        print(buffersteam[x-3:x])
