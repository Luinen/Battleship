import random

print('Ahoy Captain! Welcome to Battleship !')

# TUTORIAL 

tutorial = str(input('Do you want to read the tutorial?(aye/no)'))
print(tutorial)

def tutorial_aye():
    print('1.    ')
    print('2.    ')
    print('3.    ')
    print('4.    ')
    print('5.    ')
    print('Savvy?')

while tutorial:
    if tutorial.lower() == 'aye':
        print(tutorial_aye())
        break
    elif tutorial.lower() == 'no':
        print('Let\'s play!')
        break
    else:
        print('You have to use "aye" or "no" command')
        print(str(input('Do you want to read the tutorial?(aye/no)')))
# fix while else part

# GRID

grid = []
column_num = int(input('How many columns do you want?(5/10)'))

if column_num == 5 or 10:
    for i in range(column_num):
        grid.append(random.randint(0,100))
else:
    print('You have to use "5" or "10" numbers')
    print(column_num)
# fix column_num else part

print(grid)

for i in range(column_num):
    if grid[i] > 75:
        print('You found the enemy ship')
    elif grid[i] < 30:
        print('Only water')
    else:
        print('You found my ship')

# TARGET

target = int(input('Captain, time to shoot:(0-9)'))
print('Aye Aye Captain!')

if grid[target] > 75:
    print('Yo-ho-ho! That\'s a hit')
else:
    print('Miss!Aaaarrrrgggghhhh!')