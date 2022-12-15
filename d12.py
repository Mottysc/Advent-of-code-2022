height_letters  =  open("d12_input.txt").read().splitlines()
height_vals  =  []
for row in height_letters:
    roww  =  []
    for letter in row:
        roww.append(ord(letter)-97)
    height_vals.append(roww)
    
