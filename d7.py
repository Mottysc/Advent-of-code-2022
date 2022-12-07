cmd_output = open("d7_input.txt").read().splitlines()

filetree = []
filesizes = []
for line in cmd_output:
    if line[0].isdigit():
        size, filename = line.split(" ")
        filesizes.append(size)
totalsize = 0   
for file in filesizes:
    if int(file) < 100000:
        totalsize += int(file)
        
print(totalsize)