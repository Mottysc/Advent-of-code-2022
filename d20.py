encrypted_numbers = open("d20_input.txt").read().splitlines()
encrypted_numbers = [int(x) for x in encrypted_numbers]


for x in encrypted_numbers:
    