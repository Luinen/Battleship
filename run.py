import random
grid = []
water = 0
ally_ship = 1
opponent_ship = 2
target_user_counter = 0
target_ai_counter = 0


# CLASS
class Cell:

    """
   define the grid
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
def get_tutorial():
    tutorial = str(input('Do you want to read the tutorial?(aye/no)'))
    tutorial_condition = True
    while tutorial_condition:
        if tutorial.lower() == 'aye':
            print('')
            print('1. Welcome to Battleship: OMEGA')
            print('2. You aim to find your opponent\'s ships before it finds yours')
            print('3. You always find what you can answer at the end of each question.')
            print('4. First, you have to decide what size will be the playing field.')
            print('')
            print('5. There is only one playing field')
            print('6. After that, you have to choose the location of your ships.')
            print('7. Finally, you have to hunt down your opponent\'s ships.')
            print('The shots are marked with X, and the opponent\'s shots are marked with Y.')
            print('Have fun!!!')
            tutorial_condition = False
        elif tutorial.lower() == 'no':
            print('Let\'s play!')
            tutorial_condition = False
        else:
            print('You have to use "aye" or "no" command')
            tutorial = str(input('Do you want to read the tutorial?(aye/no)'))


# GRID
def get_grid():
    grid_size = int(input('How big should the gaming field be?(5/10):'))
    grid_condition = True
    while grid_condition:
        if grid_size == 5 or grid_size == 10:
            for cell_row in range(grid_size):
                for cell_column in range(grid_size):
                    grid.append(Cell(0, cell_row, cell_column))
            grid_condition = False
        else:
            print('You have to use "5" or "10" numbers')
            grid_size = int(input('How big should the gaming field be?(5/10):'))
    return grid_size


def display_grid(grid_size):
    print('')
    for i in range(grid_size):
        print(i, end='  ')
    print('')
    for i in range(grid_size * grid_size):
        if (i % grid_size == 0):
            print()
        if grid[i].ship == opponent_ship:
            print(water, end="  ")
        else:
            print(grid[i].ship, end='  ')
    print('')


# USER SHIP
def get_user_ship(grid_size):
    ship_counter = 0
    while ship_counter < grid_size:
        ship_row = int(input(f'Where do you want to put your ship?row 0-{grid_size-1}:'))
        ship_column = int(input(f'Where do you want to put your ship?column 0-{grid_size-1}:'))
        choosen_ship_index = grid_size*ship_row + ship_column
        if grid[choosen_ship_index].ship == ally_ship:
            print('It has already taken')
        elif (ship_row >= 0 and ship_column >= 0) and (ship_row <= grid_size-1 and ship_column <= grid_size-1):
            grid[choosen_ship_index].ship = ally_ship
            ship_counter += 1
            print('Great choice')
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
        print('Aye Aye Captain! HIT!')
        grid[target_index].ship = 'X'
        break
    elif grid[target_index].ship == water:
        print('Aye Aye Captain! MISS!')
        grid[target_index].ship = 'X'
        break
    elif grid[target_index].ship == 'X':
        print('Aye Ay......still nothing there')
        continue
    elif grid[target_index].ship == ally_ship:
        print('Stop the TRAITOR!')
        continue
    else:
        print('You can\'t shoot there')
        continue

# AI SHOOT
print('They are firing')
while True: 

    target_row = random.randint(0, grid_size - 1)
    target_column = random.randint(0, grid_size - 1)
    target_index = grid_size * target_row + target_column

    if grid[target_index].ship == ally_ship:
        print('They hit one of our ships.')
        grid[target_index].ship = 'X'
        break
    elif grid[target_index].ship == water:
        print('They don\'t know where we are! MISS')
        grid[target_index].ship = 'X'
        break
    elif grid[target_index].ship == 'X':
        continue
    else:
        continue

print('')
if grid_size == 5:
    for i in range(5):
        print(i, end='  ')
    print('')
    for i in range(grid_size * grid_size):
        if (i % 5 == 0):
            print()
        print(grid[i].ship, end="  ")
    print('')
else:
    for i in range(10):
        print(i, end='  ')
    print('')
    for i in range(grid_size * grid_size):
        if (i % 10 == 0):
            print()
        print(grid[i].ship, end="  ")
    print('')


def main():

    """
    Run all program functions
    """

    get_tutorial()
    final_grid_size = get_grid()
    display_grid(final_grid_size)
    get_user_ship(final_grid_size)

print('Welcome to Battleship: OMEGA')
main()