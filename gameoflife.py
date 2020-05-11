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


while(True):
	plt.matshow(left)
	plt.show(block=False)
	plt.pause(1)
	plt.close()
	update(right,left)
	plt.matshow(right)
	plt.show(block=False)
	plt.pause(1)
	plt.close()
	update(left,right)
