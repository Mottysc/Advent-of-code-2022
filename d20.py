encrypted_numbers = open("d20_input.txt").read().splitlines()
encrypted_numbers = [int(x) for x in encrypted_numbers]

class Number():
    def __init__(self, number: int) -> None:
        self.number = number
        self.changed = False


number_objs = [Number(x) for x in encrypted_numbers]
print(number_objs)

length_of_nums = len(number_objs)
#for x in range(length_of_nums):
    