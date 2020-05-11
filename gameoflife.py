import numpy as np
import matplotlib.pyplot as plt

xdim = 101
ydim = 82

left = np.zeros([xdim,ydim])
right= np.zeros(left.shape)

#todo: get user input
#initialise left with the desired pattern

#blinker
left[20:23,10]=1

#glider
left[30:33,50]=1
left[32,51]=1
left[31,52]=1

#glider that is close to the boundary so you can check the torus property
#left[90:93,20]=1
#left[92,21]=1
#left[91,22]=1

#r-pentomino
left[50:53,50]=1
left[50,51]=1
left[51,49]=1

'''Update the matrix a, given the current state b, using the Game of Life rules'''
def update(a,b):
	for x in range(xdim):
		for y in range(ydim):
			if(b[x,y]==0):
				if(b[x-1,y-1]+b[x-1,y]+b[x-1, (y+1)%ydim]+b[x,y-1]+b[x,(y+1)%ydim]+b[(x+1)%xdim,y-1]+b[(x+1)%xdim,y]+b[(x+1)%xdim,(y+1)%ydim] == 3):
					a[x,y]=1
				else:
					a[x,y]=0
			else: # b[x,y]=1
				if(b[x-1,y-1]+b[x-1,y]+b[x-1, (y+1)%ydim]+b[x,y-1]+b[x,(y+1)%ydim]+b[(x+1)%xdim,y-1]+b[(x+1)%xdim,y]+b[(x+1)%xdim,(y+1)%ydim] == 2 or b[x-1,y-1]+b[x-1,y]+b[x-1, (y+1)%ydim]+b[x,y-1]+b[x,(y+1)%ydim]+b[(x+1)%xdim,y-1]+b[(x+1)%xdim,y]+b[(x+1)%xdim,(y+1)%ydim] == 3):
					a[x,y]=1
				else:
					a[x,y]=0

'''Show/plot the current state of the Game, as given in matrix m'''
def showme(m):
	plt.matshow(m, fignum=0, cmap='binary')
	plt.show(block=False)
	plt.pause(0.05)


while(True):
	showme(left)
	update(right,left)
	showme(right)
	update(left,right)
