grand_total = 0
for num in range(1,16):
    calculation = num * num
    #print(f'Processing number is: {num} the square is: {calculation}')
    grand_total += calculation
    #print(grand_total)

print(f'The final sum of all squares from 1 to 15 is: {grand_total}')
