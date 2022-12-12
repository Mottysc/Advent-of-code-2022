movements = open("d9_input.txt").read().splitlines()
global head_coords, tail_coords, visited_coords
head_coords = [0, 0]
tail_coords = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

visited_coords = []

def x_too_far(knot_no):
    if knot_no == 0:
        return abs(head_coords[0] - tail_coords[0][0]) > 1
    else:
        return abs(tail_coords[0][knot_no-1] - tail_coords[0][knot_no]) > 1

def y_too_far(knot_no):
    if knot_no == 0:
        return abs(head_coords[1] - tail_coords[1][0]) > 1
    else:
        return abs(tail_coords[1][knot_no-1] - tail_coords[1][knot_no]) > 1

def move_tail():
    temp_tail = [tail_coords[0], tail_coords[1]]
    for knot_no in range(9):
        if x_too_far(knot_no):
            if head_coords[0] - tail_coords[0][knot_no] > 1:
                temp_tail[0][knot_no] += 1
            elif head_coords[0] - tail_coords[0][knot_no] < -1:
                temp_tail[0][knot_no] -= 1
                
            if head_coords[1] - tail_coords[1][knot_no] == 1:
                temp_tail[1][knot_no] += 1
            elif head_coords[1] - tail_coords[1][knot_no] == -1:
                temp_tail[1][knot_no] -= 1
            elif head_coords[1] - tail_coords[1][knot_no] == 0:
                pass
        elif y_too_far(knot_no):
            if head_coords[1] - tail_coords[1][knot_no] > 1:
                temp_tail[1][knot_no] += 1
            elif head_coords[1] - tail_coords[1][knot_no] < -1:
                temp_tail[1][knot_no] -= 1
                
            if head_coords[0] - tail_coords[0][knot_no] == 1:
                temp_tail[0][knot_no] += 1
            elif head_coords[0] - tail_coords[0][knot_no] == -1:
                temp_tail[0][knot_no] -= 1
            elif head_coords[0] - tail_coords[0][knot_no] == 0:
                pass
    
    visited_coords.append((temp_tail[0][8], temp_tail[1][8]))
    return temp_tail
        
    
print(head_coords, tail_coords)
for movement in movements:
    direction, amount = movement.split(" ")
    for x in range(int(amount)):
        if direction == "U":
            head_coords[1] += 1
            tail_coords = move_tail()
        elif direction == "D":
            head_coords[1] -= 1
            tail_coords = move_tail()
        elif direction == "L":
            head_coords[0] -= 1
            tail_coords = move_tail()
        elif direction == "R":
            head_coords[0] += 1
            tail_coords = move_tail()
        

mylist = set(visited_coords)
print(head_coords, tail_coords)
print(len(mylist))