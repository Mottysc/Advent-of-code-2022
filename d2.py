inputplays = open("d2_input.txt").read().splitlines()
opponent_moves, yourmoves = zip(*(x.split(" ") for x in inputplays))
points = 0
values = {"A": 1, "B": 2, "C": 3, "X": 0, "Y": 3, "Z": 6}
results = {"AX": 3, "AY": 4, "AZ": 8, "BX": 1, "BY": 5, "BZ": 9, "CX": 2, "CY": 6, "CZ": 7}

"""#Part 1
for x in range(len(opponent_moves)):
    if opponent_moves[x] == "A":
        if yourmoves[x] == "Y":
            points += 8
        elif yourmoves[x] == "X":
            points += 4
        else: 
            points += 3
    elif opponent_moves[x] == "B":
        if yourmoves[x] == "Z":
            points += 9
        elif yourmoves[x] == "Y":
            points += 5
        else: 
            points += 1
    elif opponent_moves[x] == "C":
        if yourmoves[x] == "X":
            points += 7
        elif yourmoves[x] == "Z":
            points += 6
        else: 
            points += 2

print(points)"""
# Part 2
for x in range(len(opponent_moves)):
    points += results[opponent_moves[x]+yourmoves[x]]

print(points)