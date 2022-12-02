import random

print('Ahoy Captain! Welcome to Battleship !')
tutorial = print(str(input('Do you want to read the tutorial?(aye/no)')))

if tutorial == 'aye':
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
    if  grid[i] > 75:
        print('You found the enemy ship')
    elif grid[i] < 30:
        print('Only water')
    else:
        print('You found my ship')

target = int(input('Captain, time to shoot:'))

if grid[target] > 75:
    print('Yo-hoo-ho! That\'s a hit')
else:
    print('Miss!Aaaarrrrgggghhhh!')