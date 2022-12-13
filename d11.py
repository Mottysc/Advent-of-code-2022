monkey_stats = open("d11_input.txt").read()

signs_dict = {"divisible": lambda x, y : True if x % y == 0 else False, "*": lambda x, y: x * y, "/": lambda x, y: x / y, "+": lambda x, y: x + y}


class Monkey():
    def __init__(self, id: int, holding: list, operation: str, test: str, testtrue: int, testfalse: int) -> None:
        self.id = id
        self.holding = holding
        self.operation = operation
        self.test = test
        self.testtrue = testtrue
        self.testfalse = testfalse
        self.IsIn = True
        self.NumberOfIns = 0
    
    def do_operation(self):
        operation_str = self.operation
        first_v, sign, second_v = operation_str.split(" ")
        if first_v == "old":
            first_v = self.holding[0]
            
        if second_v == "old":
            second_v = self.holding[0]
        print(f"- Monkey inspects an item with a worry level of {self.holding[0]}")
        new_val = signs_dict[sign](self.holding[0], int(second_v))
        print(f"- - Worry level is {sign} by {second_v} to {new_val}.")
        new_val = new_val//3
        print(f"- - Worry level is divided by 3 to {new_val}")
        self.NumberOfIns += 1
        self.holding[0] = new_val
        
    def do_test(self):
        first_v, second_v = self.test.split(" by ")
        if signs_dict["divisible"](int(self.holding[0]), int(second_v)):
            print(f"- - Current worry level is divisible by {second_v}")
            print(f"- - Item with worry level {self.holding[0]} is thrown to monkey {self.testtrue}.\n")
            return self.testtrue
        else:
            print(f"- - Current worry level is not divisible by {second_v}")
            print(f"- - Item with worry level {self.holding[0]} is thrown to monkey {self.testfalse}.\n")
            return self.testfalse
    
    def receive_item(self, item: int):
        self.holding.append(item)
        
    def give_item(self):
        return self.holding.pop(0)

global active_monkeys
active_monkeys = [
    Monkey(0, [74, 64, 74, 63, 53], "old * 7", "divisible by 5", 1, 6),
    Monkey(1, [69, 99, 95, 62], "old * old", "divisible by 17", 2, 5),
    Monkey(2, [59, 81], "old + 8", "divisible by 7", 4, 3),
    Monkey(3, [50, 67, 63, 57, 63, 83, 97], "old + 4", "divisible by 13", 0, 7),
    Monkey(4, [61, 94, 85, 52, 81, 90, 94, 70], "old + 3", "divisible by 19", 7, 3),
    Monkey(5, [69], "old + 5", "divisible by 3", 4, 2),
    Monkey(6, [54, 55, 58], "old + 7", "divisible by 11", 1, 5),
    Monkey(7, [79, 51, 83, 88, 93, 76], "old * 3", "divisible by 2", 0, 6)
]
global inactive_monkeys
inactive_monkeys = []
roundlog = []
for round_n in range(20):
    for monkey in active_monkeys:
        if len(monkey.holding) == 0:
            inactive_monkeys.append(active_monkeys.pop(active_monkeys.index(monkey)))
        else:
            print(f"Monkey {monkey.id}:")
            for item in monkey.holding:
                monkey.do_operation()
                try:
                    active_monkeys[monkey.do_test()].receive_item(monkey.give_item())
                except IndexError:
                    pass
    roundlog.append([monk.id for monk in active_monkeys])

print("\n".join([f"{num}: {monks}" for num, monks in enumerate(roundlog)]))
print(sorted([monk.NumberOfIns for monk in active_monkeys], reverse=True))
print(sorted([monk.NumberOfIns for monk in inactive_monkeys], reverse=True))
