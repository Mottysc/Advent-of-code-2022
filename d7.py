cmd_output = open("d7_input.txt").read().splitlines()

filetree = {}
current_dir = []
for line in cmd_output:
    command = line.split(" ")
    if command[0] == "$":
        if command[1] == "cd":
            if command[2] != "..":
                if len(current_dir) == 0:
                    current_dir.append(command[2])
                    filetree[command[2]] = []
                else:
                    current_dir.append(command[2])
                    filetree[0][current_dir[-1]].append({command[2]: []})
            else:
                current_dir.pop()
    elif command[0] == "dir":
        if command[1] not in filetree[current_dir[-1]]:
            filetree[current_dir[-1]].append({command[1]: []})
    elif command[0].isdigit():
        filetree[current_dir].append({command[1]: command[0]})
        
print(filetree)
