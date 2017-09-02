import numpy as np
c = int(input("Enter no of cities : "))
matrix = np.array([[1,2,3,4],[5,6,7,8],[3,4,5,6],[9,8,4,3]])
def fact(c):
	if(c==1):
		return 1
	return c*fact(c-1)
n = fact(c)
count = 0
cost = np.zeros(shape=(n,2), dtype=np.int_)
def path(nc, visit, psum, route, num):
	global count, matrix
	flag = 0
	for i in range(c):
		if(visit[i]==0 and num <= c): 
			flag = 1 
			visit[i] = 1
			num += 1
			psum = psum + matrix[nc][i]
			route = route*10+(i+1)
			path(i,visit, psum, route, num)
			visit[i] = 0
			num -= 1
			route = route/10
	if(flag==0):
		cost[count][0] = psum
		cost[count][1] = route
		count += 1
		return
def start():
	for i in range(c):
		visit = [0,0,0,0]
		visit[i] = 1
		route = i+1
		path(i,visit, 0,route, 1)
start()
print matrix
mincost =  np.min(cost, axis = 0)
#print mincost[0]
##print mincost[1]
mini = 100
rout = 0
for i in range(len(cost)):
	if mini>cost[i][0]:
		mini = cost[i][0]
		rout = cost[i][1]
print "Min Cost = ",mini
print "Path = ",rout
