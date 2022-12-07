buffersteam = open("d6_input.txt").read()
letters = []

for x in range(4, len(buffersteam)):
    current_letter = buffersteam[x]
    if len(letters) < 3:
        letters.extend(buffersteam[:x-1])
    else:
        letters.clear()
        letters.extend(buffersteam[x-4:x])
        
    if current_letter in letters:
        pass
    else:
        print(letters)
