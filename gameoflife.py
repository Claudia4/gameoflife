import numpy as np
import matplotlib.pyplot as plt

xdim = 101
ydim = 82

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


# glider that is close to the boundary so you can check the torus property
# left[90:93,20]=1
# left[92,21]=1
# left[91,22]=1


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
            if (b[x, y] == 0):
                if (b[x - 1, y - 1] + b[x - 1, y] + b[x - 1, (y + 1) % ydim] + b[x, y - 1] + b[x, (y + 1) % ydim] + b[
                    (x + 1) % xdim, y - 1] + b[(x + 1) % xdim, y] + b[(x + 1) % xdim, (y + 1) % ydim] == 3):
                    a[x, y] = 1
                else:
                    a[x, y] = 0
            else:  # b[x,y]=1
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
