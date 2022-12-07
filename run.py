import random

class Cell:

    """
    define the grid

    0 -water, empty space
    1 -own ship
    2 -enemy ship
    """
    def __init__(self, ship, cell_row, cell_column):
        self.ship = 0
        self.cell_row = cell_row
        self.cell_column = cell_column




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

#  0 - water, empty space
#  1 - own ship
#  2 - enemy ship