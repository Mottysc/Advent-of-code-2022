buffersteam = open("d6_input.txt").read()
letters = []

for x in range(4, len(buffersteam)):
    current_letter = buffersteam[x]
    if len(letters) < 4:
        letters.extend(buffersteam[:x])
    else:
        
    
    if current_letter in letters:
        pass
    else:
        print(buffersteam[x-4:x])
