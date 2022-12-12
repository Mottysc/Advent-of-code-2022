registry_cmds = open("d10_input.txt").read().splitlines()

signals = [1]
crt_pixel = []
global regX
regX = 1

for x in range(len(registry_cmds)):
    if registry_cmds[x] == "noop":
        signals.append(regX)
    else:
        addx, amount = registry_cmds[x].split(" ")
        signals.append(regX)
        regX += int(amount)
        signals.append(regX)

## p2

for x in range(len(signals)):
    if abs(x%40 - signals[x]) < 2:
        crt_pixel.append("█")
    else:
        crt_pixel.append(".")
        
crt_matrix = [crt_pixel[i:i + 40] for i in range(0, len(crt_pixel), 40)]
crt_strings = []
for x in crt_matrix:
    crt_strings.append("".join(x))

print("\n".join(crt_strings))

#print(signals)
#print(len(signals), len(registry_cmds))
#print([signals[19], signals[59], signals[99], signals[139], signals[179], signals[219]])
#print(sum([signals[19], signals[59], signals[99], signals[139], signals[179], signals[219]]))
#print([signals[19]*20, signals[59]*60, signals[99]*100, signals[139]*140, signals[179]*180, signals[219]*220])
print(sum([signals[19]*20, signals[59]*60, signals[99]*100, signals[139]*140, signals[179]*180, signals[219]*220]))