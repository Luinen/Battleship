import random

print('Welcome to Battleship game!')
tutorial = print(str(input('Do you want to read the tutorial?(yes/no)')))

if tutorial == 'yes':
    pass
elif tutorial == 'no':
    print('Let\'s play!')
else:
    print('You have to use "yes" or "no" command')

grid = []
column_num = int(input('How many columns do you want?'))

for i in range(column_num):
    grid.append(random.randint(0,100))

print(grid)

for i in range(column_num):
    if  grid[i] > 50:
        print('You found the enemy ship')
    else:
        print('You found my ship')