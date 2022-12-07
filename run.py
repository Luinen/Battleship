import random

# CLASS
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


battleship = """
(            )    )  (              )              
 ( )\     )  ( /( ( /(  )\   (      ( /( (            
 )((_) ( /(  )\()))\())((_) ))\ (   )\()))\  `  )     
((_)_  )(_))(_))/(_))/  _  /((_))\ ((_)\((_) /(/(  _  
 | _ )((_)_ | |_ | |_  | |(_)) ((_)| |(_)(_)((_)_\(_) 
 | _ \/ _` ||  _||  _| | |/ -_)(_-<| ' \ | || '_ \)_  
 |___/\__,_| \__| \__| |_|\___|/__/|_||_||_|| .__/(_) 
         )     *                            |_|       
      ( /(   (  `         (        (                  
      )\())  )\))(   (    )\ )     )\                 
     ((_)\  ((_)()\  )\  (()/(  ((((_)(               
       ((_) (_()((_)((_)  /(_))_ )\ _ )\              
      / _ \ |  \/  || __|(_)) __|(_)_\(_)             
     | (_) || |\/| || _|   | (_ | / _ \               
      \___/ |_|  |_||___|   \___|/_/ \_\
"""
print(battleship)

# TUTORIAL
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

# GRID
grid = []
grid_size = int(input('How big should the playfield be?(5/10):'))

while True:
    if grid_size == 5 or grid_size == 10:
        for cell_row in range(grid_size):
            for cell_column in range(grid_size):
                grid.append(Cell(0, cell_row, cell_column))
        break
    else:
        print('You have to use "5" or "10" numbers')
        grid_size = int(input('How many columns do you want?(5/10):'))


for i in range(grid_size*grid_size):
    if(i%5==0):
        print()
    print(grid[i].ship, end="  ")
print('')


water = 0
ally_ship = 1
opponent_ship = 2

# USER SHIP
ship_counter = 0
while ship_counter < grid_size:

    ship_row = int(input(f'Where do you want to put your ship?row 0-{grid_size-1}:'))
    ship_column = int(input(f'Where do you want to put your ship?columns 0-{grid_size-1}:'))
    choosen_ship_index = grid_size*ship_row + ship_column

    if grid[choosen_ship_index].ship == ally_ship:
        continue    
    elif (ship_row >= 0 and ship_column >= 0) and (ship_row <= grid_size-1 and ship_column <= grid_size-1):
        grid[choosen_ship_index].ship = ally_ship
        ship_counter += 1
    else:
        print('Use numbers in the specified range')

# AI SHIP
ship_counter = 0
while ship_counter < grid_size:

    ship_row = random.randint(0,grid_size-1)
    ship_column = random.randint(0,grid_size-1)
    choosen_ship_index = grid_size*ship_row + ship_column

    if grid[choosen_ship_index].ship == ally_ship or grid[choosen_ship_index].ship == opponent_ship:
        continue
    else:
        grid[choosen_ship_index].ship = opponent_ship
        ship_counter += 1

# battlefield
for i in range(grid_size*grid_size):
    if(i%5==0):
        print()
    print(grid[i].ship, end="  ")
print('')

# USER SHOOT
while True: 

    target_row = int(input(f'Captain, time to shoot, row 0-{grid_size - 1}:'))
    target_column = int(input(f'Captain, time to shoot, column 0-{grid_size - 1}:'))
    target_index = grid_size * target_row + target_column

    if grid[target_index].ship == opponent_ship:
        print('hit')
        grid[target_index].ship = 'X'
        break
    elif grid[target_index].ship == water:
        print('miss')
        grid[target_index].ship = 'X'
        break
    elif grid[target_index].ship == 'X':
        print('Still nothing')
        continue
    elif grid[target_index].ship == ally_ship:
        print('Stop the TRAITOR!')
        continue
    else:
        print('You can\'t shoot there')
        continue

# AI SHOOT
while True: 

    target_row = random.randint(0, grid_size - 1)
    target_column = random.randint(0, grid_size - 1)
    target_index = grid_size * target_row + target_column

    if grid[target_index].ship == ally_ship:
        print('hit')
        grid[target_index].ship = 'X'
        break
    elif grid[target_index].ship == water:
        print('miss')
        grid[target_index].ship = 'X'
        break
    elif grid[target_index].ship == 'X':
        print('Still nothing')
        continue
    else:
        print('You can\'t shoot there')
        continue

for i in range(grid_size*grid_size):
    if(i%5==0):
        print()
    print(grid[i].ship, end="  ")
print('')