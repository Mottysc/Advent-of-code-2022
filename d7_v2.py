cmd_output = open("d7_input.txt").read().splitlines()
import os
current_dir = []
for line in cmd_output:
    command = line.split(" ")
    if command[0] == "$":
        if command[1] == "cd":
            if command[2] == "..":
                current_dir.pop()
            elif command[2] == "/":
                current_dir.append(command[2])
            else:
                current_dir.append(command[2])
                path_to_make = "C:/Users/motty/OneDrive/Desktop/code-testing-ground/Advent of code/Advent of code 2022/filess/"+"/".join(current_dir)
                os.makedirs(path_to_make, exist_ok=True)
    elif command[0] == "dir":
            path_to_make = "C:/Users/motty/OneDrive/Desktop/code-testing-ground/Advent of code/Advent of code 2022/filess/"+"/".join(current_dir)
            os.makedirs(path_to_make, exist_ok=True)
    elif command[0].isdigit():
            path_to_make = "C:/Users/motty/OneDrive/Desktop/code-testing-ground/Advent of code/Advent of code 2022/filess/"+"/".join(current_dir) + "/" + command[1]
            with open(path_to_make, "w") as f:
                f.close()
            
        
print(current_dir)