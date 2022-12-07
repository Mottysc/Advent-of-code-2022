global s1, s2, s3, s4, s5, s6, s7, s8, s9
s1 = ['S', 'L', 'W']
s2 = ['J', 'T', 'N', 'Q']
s3 = ['S', 'C', 'H', 'F', 'J']
s4 = ['T', 'R', 'M', 'W', 'N', 'G', 'B']
s5 = ['T', 'R', 'L', 'S', 'D', 'H', 'Q', 'B']
s6 = ['M', 'J', 'B', 'V', 'F', 'H', 'R', 'L']
s7 = ['D', 'W', 'R', 'N', 'J', 'M']
s8 = ['B', 'Z', 'T', 'F', 'H', 'N', 'D', 'J']
s9 = ['H', 'L', 'Q', 'N', 'B', 'F', 'T']

"""instructions = open("d5_input.txt").read().splitlines()
stack_id = {"1" : s1, "2" : s2, "3" : s3, "4" : s4, "5" : s5, "6" : s6, "7" : s7, "8" : s8, "9" : s9}
for ins_line in instructions:
    count, start_stack, end_stack = ins_line.split(",")
    for x in range(int(count)):
        crate = stack_id[start_stack].pop()
        stack_id[end_stack].append(crate)"""
        
instructions = open("d5_input.txt").read().splitlines()

stack_id = {"1": s1, "2": s2, "3": s3, "4": s4, "5": s5, "6": s6, "7": s7, "8": s8, "9": s9}
for ins_line in instructions:
    count, start_stack, end_stack = ins_line.split(",")
    print(s1, s2, s3, s4, s5, s6, s7, s8, s9)
    start_stack_used = stack_id[start_stack]
    crates_to_move = start_stack_used[-int(count):]
    stack_id[start_stack] = start_stack_used[:-int(count)]
    stack_id[end_stack].extend(crates_to_move)
    
s1 = stack_id["1"]
s2 = stack_id["2"]
s3 = stack_id["3"]
s4 = stack_id["4"]
s5 = stack_id["5"]
s6 = stack_id["6"]
s7 = stack_id["7"]
s8 = stack_id["8"]
s9 = stack_id["9"]

print(s1, s2, s3, s4, s5, s6, s7, s8, s9)
print(s1[-1]+s2[-1]+s3[-1]+s4[-1]+s5[-1]+s6[-1]+s7[-1]+s8[-1]+s9[-1])