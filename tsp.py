import numpy as np
n = 4
matrix = np.array([[1,2,3,4],[5,6,7,8],[3,4,5,6],[9,8,4,3]])
visit = np.array([0,0,0,0])
cost = 0
def nextcity(c):
	mini = 999
	nc = 999
	kmin = 0
	global cost, matrix, visit
	for i in range(n):
		if((matrix[c][i] != 0)) and ((visit[i] == 0)):
			if(matrix[c][i]<mini):
				mini = matrix[c][i]+matrix[0][c]
				kmin = matrix[c][i]
				nc = i
	cost += kmin 
	return nc			
def mincost(city):
	global cost, matrix
	print (city+1)
	visit[city] = 1
	nc = nextcity(city)
	if(nc == 999):
		nc = 0
		print (nc+1)
		cost += matrix[city][nc]
		print "Cost %d" % cost
		return
	mincost(nc)
print matrix
print "The Path is : "
mincost(0)