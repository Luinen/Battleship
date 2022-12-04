"""
for i in range(column_num):
    if grid[i] == 0:
        print('Only Water')
    elif grid[i] == 1:
        print('You found my ship')
    elif grid[i] == 2:
        print('You found the enemy ship')

target = int(input('Captain, time to shoot:(0-9)'))
print('Aye Aye Captain!')

if grid[target] == 2:
    print('Yo-ho-ho! That\'s a hit')
else:
    print('Miss!Aaaarrrrgggghhhh!')

search_row= 2
search_column= 1
search_element_index= grid_size*search_row+ search_column
print(search_element_index)
print(grid[grid_size*search_row+search_column].cell_row, grid[grid_size*search_row+search_column].cell_column)

ship_row =int(input(f'Where do you want to put your ship?row 0-{grid_size-1}:'))
ship_column = int(input(f'Where do you want to put your ship?column 0-{grid_size-1}:'))

ship_location= grid_size*ship_row+ship_column
print(ship_location)

grid[ship_location].contain= 1
print(grid[ship_location].contain)

ship_counter = 0
while ship_counter < grid_size:
    if (cell_row >= 0 and cell_column >= 0) and (cell_row <= grid_size-1 and cell_column <= grid_size-1):
        cell_row = int(input(f'Where do you want to put your ship?row 0-{grid_size-1}:'))
        cell_column = int(input(f'Where do you want to put your ship?columnc 0-{grid_size-1}:'))
#        own_ship = 1
        ship_counter += 1

        print('Use the specified range')
"""

import random

class Cell:

    """
    define the grid

    0 -water, empty space
    1 -own ship
    2 -enemy ship
    """
    def __init__(self, contain, cell_row, cell_column):
        self.contain = 0
        self.cell_row = cell_row
        self.cell_column = cell_column


def get_tutorial():

    tutorial = str(input('Do you want to read the tutorial?(aye/no)'))

    while True:

        if tutorial.lower() == 'aye':
            print('1.Rules')
            print('2.')
            print('3.')
            break
        elif tutorial.lower() == 'no':
            print('Let\'s play!')
            break
        else:
            print('You have to use "aye" or "no" command')
            tutorial = str(input('Do you want to read the tutorial?(aye/no)'))


def get_grid():

    grid = []
    grid_size = int(input('How many columns do you want?(5/10):'))

    while True:
        if grid_size == 5 or grid_size == 10:
            for cell_row in range(grid_size):
                for cell_column in range(grid_size):
                    grid.append(Cell(0, cell_row, cell_column))
            break
        else:
            print('You have to use "5" or "10" numbers')
            grid_size = int(input('How many columns do you want?(5/10):'))

    return print(grid)


def main():
    """
    Run all program functions
    """
    get_tutorial()
    get_grid()


print('Ahoy Captain! Welcome to Battleship!')
main()