valves = {
    "AA": ["DD", "II", "BB"],
    "BB": ["CC", "AA"],
    "CC": ["DD", "BB"],
    "DD": ["CC", "AA", "EE"],
    "EE": ["FF", "DD"],
    "FF": ["EE", "GG"],
    "GG": ["FF", "HH"],
    "HH": ["GG"],
    "II": ["AA", "JJ"],
    "JJ": ["II"]
    }
pressures = {
    "AA": 0,
    "BB": 13,
    "CC": 2,
    "DD": 20,
    "EE": 3,
    "FF": 0,
    "GG": 0,
    "HH": 22,
    "II": 0,
    "JJ": 21
    }

class Valve():
    def __init__(self, name:str, pressure: int, leadsto: list) -> None:
        self.ID = name
        self.pressure = pressure
        self.leads_to = leadsto
        self.closed = True
        
    def change_state(self):
        self.closed = False if self.closed == True else False
global Valves
Valves = {
    "AA": Valve ("AA", 0, ["DD", "II", "BB"]),
    "BB": Valve ("BB", 13, ["CC", "AA"]),
    "CC": Valve ("CC", 2, ["DD", "BB"]),
    "DD": Valve ("DD", 20, ["CC", "AA", "EE"]),
    "EE": Valve ("EE", 3, ["FF", "DD"]),
    "FF": Valve ("FF", 0, ["EE", "GG"]),
    "GG": Valve ("GG", 0, ["FF", "HH"]),
    "HH": Valve ("HH", 22, ["GG"]),
    "II": Valve ("II", 0, ["AA", "JJ"]),
    "JJ": Valve ("JJ", 21,  ["II"])
    }
    

global time_left, current_room, Visited_rooms, total_pressure
time_left = 30
current_room = "AA"
total_pressure = 0
Visited_rooms = []

def change_rooms(current_room, time_left):
    next_room = [next_valve for next_valve in Valves[current_room].leads_to if next_valve not in Visited_rooms]
    if next_room:
        time_left -= 1
        print(f"moving rooms")
        current_room = next_room[0]
        print(f"going to {current_room}")
        return time_left, current_room
    else:
        
        potential_valves = [[(second_next_valve, first_next) for second_next_valve in Valves[first_next].leads_to if second_next_valve not in Visited_rooms] for first_next in Valves[current_room].leads_to]
        cleaned_valves = [x for x in potential_valves if x]
        print(cleaned_valves)
        current_room = [x[1] for x in cleaned_valves[0]][0]
        print(f"going to {current_room} to get to {[x[0] for x in cleaned_valves[0]][0]}")
        return time_left, current_room
        
            
            

for i in range(30):
    print(f"minute: {31-time_left}")
    print("visited: ", ", ".join(Visited_rooms))
    print(f"in room {current_room}")
    if Valves[current_room].pressure == 0:
        print(f"has no pressure {current_room}")
        Visited_rooms.append(current_room)
        time_left, current_room = change_rooms(current_room, time_left)
        
    else:
        print(f"{current_room} valve has pressure")
        if Valves[current_room].closed:
            print(f"opening {current_room} valve...")
            time_left -= 1
            Valves[current_room].change_state()
            total_pressure += time_left*Valves[current_room].pressure
            print(f"pressure is now {total_pressure}")
            Visited_rooms.append(current_room)
            time_left, current_room = change_rooms(current_room, time_left)
        else:
            print(f"{current_room} valve is open")
            Visited_rooms.append(current_room)
            time_left, current_room = change_rooms(current_room, time_left)
    print("\n\n")      
print(total_pressure)