'''
Game of Life Simluation by Annika Hennes and Claudia Bischoff

Compile: No compilation needed
Run: python3 gameoflife.py
    input the number of the desired starting pattern when prompted
    to abort the program, close the plotting window
'''

import numpy as np
import matplotlib.pyplot as plt

xdim = 101
ydim = 82

# The grid for the game of life is stored as an array containing the numbers 0 or 1
# we use two grids (left and right) in order to do the simultaneous updates of all cells correctly, alternating from one grid to the other
left = np.zeros([xdim, ydim])
right = np.zeros(left.shape)


# initialise left with the desired pattern

# blinker
def init_blinker(left):
    left[20:23, 10] = 1
    return left

# glider
def init_glider(left):
    left[30:33, 50] = 1
    left[32, 51] = 1
    left[31, 52] = 1
    return left

# r-pentomino
def init_r_pentomino(left):
    left[50:53, 50] = 1
    left[50, 51] = 1
    left[51, 49] = 1
    return left

# Gosper's Glidergun
def init_gospers_glidergun(left):
    pos_left_stopblock = (5, 10)
    x, y = pos_left_stopblock
    left[x:(x + 2), y:(y + 2)] = 1  # left stop block
    # left side of main part
    left[x:(x + 3), (y + 10)] = 1
    left[x - 1, y + 11] = 1
    left[x + 3, y + 11] = 1
    left[x - 2, (y + 12):(y + 14)] = 1
    left[x + 4, (y + 12):(y + 14)] = 1
    left[x + 1, y + 14] = 1
    left[x - 1, y + 15] = 1
    left[x + 3, y + 15] = 1
    # left side of main part
    left[x:(x + 3), y + 16] = 1
    left[x + 1, y + 17] = 1
    left[(x - 2):(x + 1), (y + 20):(y + 22)] = 1
    left[x - 3, y + 22] = 1
    left[x + 1, y + 22] = 1
    left[(x - 4):(x - 2), y + 24] = 1
    left[(x + 1):(x + 3), y + 24] = 1
    # right stop block
    left[(x - 2):x, (y + 34):(y + 36)] = 1
    return left

#bunnies
def init_bunnies(left):
    x, y = [20,30]
    left[x,y]=1
    left[x+2,y+1:y+3]=1
    left[x+6,y:y+2]=1
    left[x+1,y+3]=1
    left[x+3,y+3]=1
    left[x+5,y+2]=1
    left[x+7,y+2]=1
    return left

'''Update the matrix a, given the current state b, using the Game of Life rules'''
def update(a, b):
    for x in range(xdim):
        for y in range(ydim):
            if (b[x, y] == 0): #cetre cell is dead
                if (b[x - 1, y - 1] + b[x - 1, y] + b[x - 1, (y + 1) % ydim] + b[x, y - 1] + b[x, (y + 1) % ydim] + b[
                    (x + 1) % xdim, y - 1] + b[(x + 1) % xdim, y] + b[(x + 1) % xdim, (y + 1) % ydim] == 3):
                    a[x, y] = 1
                else:
                    a[x, y] = 0
            else:  # b[x,y]=1 cetre cell is alive
                if (b[x - 1, y - 1] + b[x - 1, y] + b[x - 1, (y + 1) % ydim] + b[x, y - 1] + b[x, (y + 1) % ydim] + b[
                    (x + 1) % xdim, y - 1] + b[(x + 1) % xdim, y] + b[(x + 1) % xdim, (y + 1) % ydim] == 2 or b[
                    x - 1, y - 1] + b[x - 1, y] + b[x - 1, (y + 1) % ydim] + b[x, y - 1] + b[x, (y + 1) % ydim] + b[
                    (x + 1) % xdim, y - 1] + b[(x + 1) % xdim, y] + b[(x + 1) % xdim, (y + 1) % ydim] == 3):
                    a[x, y] = 1
                else:
                    a[x, y] = 0


'''Show/plot the current state of the Game, as given in matrix m'''
def showme(m):
    plt.matshow(m, fignum=0, cmap='binary')
    plt.show(block=False)
    plt.pause(0.05)

# The acutal simulation starts here
# First get the user input and initialise the grid, using the above init functions
print("Patterns:\n"
      "(1) Blinker\n"
      "(2) Glider\n"
      "(3) R Pentomino\n"
      "(4) Glidergun\n"
      "(5) Bunnies")
choice = int(input("Choose one of the above patterns using the respective number:"))
if choice == 1:
    left = init_blinker(left)
elif choice == 2:
    left = init_glider(left)
elif choice == 3:
    left = init_r_pentomino(left)
elif choice == 4:
    left = init_gospers_glidergun(left)
elif choice == 5:
    left = init_bunnies(left)
else:
    print("Input not valid.")

# run the simulation by updating from left to right and from right to left in an alternating fashion
# in between the updates, write the number of living cells to a file and show the current state in a plot
with open('n_of_living_cells.txt', 'w') as f:
    while True:
        n = int(sum(sum(left)))
        f.write(str(n) + "\n")
        showme(left)
        update(right, left)
        n = int(sum(sum(right)))
        f.write(str(n) + "\n")
        showme(right)
        update(left, right)
