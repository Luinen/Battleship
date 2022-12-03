import random

print('Ahoy Captain! Welcome to Battleship !')

# TUTORIAL 

tutorial = str(input('Do you want to read the tutorial?(aye/no)'))
print(tutorial)

while True:
    if tutorial.lower() == 'aye':
        print('1.')
        print('2.')
        print('3.')
        break
    elif tutorial.lower() == 'no':
        print('Let\'s play!')
        break
    else:
        print('You have to use "aye" or "no" command')
        tutorial = str(input('Do you want to read the tutorial?(aye/no)'))

# GRID

grid = []
column_num = int(input('How many columns do you want?(5/10)'))

if column_num == 5 or 10:
    for i in range(column_num):
        grid.append(random.randint(0,2))
else:
    print('You have to use "5" or "10" numbers')
    print(column_num)
# fix column_num else part

print(grid)

for i in range(column_num):
    if grid[i] == 0:
        print('Only Water')
    elif grid[i] == 1:
        print('You found my ship')
    elif grid[i] == 2:
        print('You found the enemy ship')

# TARGET

target = int(input('Captain, time to shoot:(0-9)'))
print('Aye Aye Captain!')

if grid[target] == 2:
    print('Yo-ho-ho! That\'s a hit')
else:
    print('Miss!Aaaarrrrgggghhhh!')