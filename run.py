grid = []
print(grid)

column_num = int(input('How many columns do you want?'))

for i in range(column_num):
    grid.append(random.randint(0,100))