movements = open("d9_input.txt").read().splitlines()
global head_coords, tail_coords, visited_coords
head_coords = [0, 0]
tail_coords = [0, 0]

visited_coords = []
def x_too_far():
    return abs(head_coords[0] - tail_coords[0]) > 1

def y_too_far():
    return abs(head_coords[1] - tail_coords[1]) > 1

def move_tail():
    temp_tail = [tail_coords[0], tail_coords[1]]
    if x_too_far():
        if head_coords[0] - tail_coords[0] > 1:
            temp_tail[0] += 1
        elif head_coords[0] - tail_coords[0] < -1:
            temp_tail[0] -= 1
            
        if head_coords[1] - tail_coords[1] == 1:
            temp_tail[1] += 1
        elif head_coords[1] - tail_coords[1] == -1:
            temp_tail[1] -= 1
        elif head_coords[1] - tail_coords[1] == 0:
            pass
    elif y_too_far():
        if head_coords[1] - tail_coords[1] > 1:
            temp_tail[1] += 1
        elif head_coords[1] - tail_coords[1] < -1:
            temp_tail[1] -= 1
            
        if head_coords[0] - tail_coords[0] == 1:
            temp_tail[0] += 1
        elif head_coords[0] - tail_coords[0] == -1:
            temp_tail[0] -= 1
        elif head_coords[0] - tail_coords[0] == 0:
            pass
    
    visited_coords.append(tuple(temp_tail))
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
print(len(mylist))