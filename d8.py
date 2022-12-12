tree_input = [list(x) for x in open("d8_input.txt").read().splitlines()]
rows = []
columns = []
largest_trees = []

for column in range(1, 97):
    for row in range(1, 97):
        size = tree_input[row][column]
        