tree_input = [list(x) for x in open("d8_input.txt").read().splitlines()]
rows = []
columns = []

largest_trees = []

for column in range(99):
    temp = []
    for row in range(99):
        temp.append(tree_input[row][column])
    columns.append(temp)

rows_reverse = tree_input
rows_reverse.reverse()
columns_reverse = columns
columns_reverse.reverse()
for row in tree_input:
    largest_trees.append((tree_input.index(row), row.index(max(row))))

for row in range(99):
    row_inq = rows_reverse[row]
    largest_trees.append((98-row, 98-int(rows_reverse[row].index(max(row_inq)))))

for row in columns:
    largest_trees.append((row.index(max(row)), columns.index(row)))

for row in range(99):
    row_inq = columns_reverse[row]
    largest_trees.append((98-int(columns_reverse[row].index(max(row_inq))), 98-row))

mylist = list(dict.fromkeys(largest_trees))

import numpy as np
import matplotlib.pyplot as plt

xcords = [x[0] for x in mylist]
ycords = [y[1] for y in mylist]
weights = [1]*len(xcords)
print(xcords)
print(ycords)
plt.hist2d(x=xcords, y=ycords, weights=weights)

plt.show()

