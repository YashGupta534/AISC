import numpy as np
import random
print "     Tic - Tac - Toe"
print "Player - 1 || Computer - 0"
switch = 0

def pmove():
	global play, count, pos, v
	st_arr = raw_input("Enter position in X,Y ").split(',')
	co_or = [int(num) for num in st_arr]
	if(play[co_or[0]][co_or[1]] == v):
		count += 1
		play[co_or[0]][co_or[1]] = 1
		msq = magic[co_or[0]][co_or[1]]
		pos.append(msq)
	else:
		print "Somebody already played here"
		pmove()
	disp()
	chkwin()
	cmove()

def cmove():
	global count, pos, magic, v, comp, switch
	if(count >= switch):
		tot = 0 
		last = 0
		loopbr = False
		for i in pos:
			tot = 0
			for j in pos:
				if i != j and (i+j)<=14:
					tot = i+j
					last = 15 - tot
					if last > 9:
						continue
					if last in comp:
						break
					if last != i and last != j:
						#print "Last = ", last
						#print "i = ",i
						#print "j = ",j
						loopbr = True
						break
			if loopbr == True:
				break
		#print pos
		#print comp		
		loopbr = False	
		if last in comp:
			#print "yash ", last
			playrandom()	
		else:
			for i in range(len(magic)):
				for j in range(len(magic)):
					if magic[i][j] == last:
						if play[i][j] == v:
							play[i][j] = 0
							comp.append(magic[i][j])
							count = count + 1 
							loopbr = True
							break
				if loopbr == True:
					break
		disp()
		chkwin()
		pmove()
	elif count < switch:
		c = count
		ftm = {1:center, 2:luc, 3:ruc, 4:ldc, 5:rdc}
		m = random.randrange(1, 6, 1)
		ftm[m]()
		if(c == count):
			cmove()
		else:
			disp()
			chkwin()
			pmove()

def center():
	global play, count, v, comp, magic
	if(play[1][1] == v):
		count += 1
		play[1][1] = 0
		comp.append(magic[1][1])
	else:
		return

def luc():
	global play, count, v, comp, magic
	if(play[0][0] == v):
		count += 1
		play[0][0] = 0
		comp.append(magic[0][0])
	else:
		return

def ruc():
	global play, count, v, comp, magic
	if(play[0][2] == v):
		count += 1
		play[0][2] = 0
		comp.append(magic[0][2])
	else:
		return

def ldc():
	global play, count, v, comp, magic
	if(play[2][0] == v):
		count += 1
		play[2][0] = 0
		comp.append(magic[2][0])
	else:
		return

def rdc():
	global play, count, v, comp, magic
	if(play[2][2] == -1):
		count += 1
		play[2][2] = 0
		comp.append(magic[2][2])
	else:
		return

def wrap(i):
	if i == 2:
		i = 0
		return i
	elif i == 0:
		i = 2 
		return i

def playrandom():
	global play, v, count
	loopbr = False
	for i in [0,1,2]:
		for j in [0,1,2]:
			if play[i][j] == v:
				play[i][j] = 0
				count += 1
				loopbr = True
				break
		if loopbr == True:
			break
	disp()
	chkwin()
	pmove()

def disp():
	global play
	print play
	return

def chkwin():
	global play, count, v
	for i in range(len(play)):
		tot = v
		for j in range(len(play)):
			tot = tot + play[i][j]+2
		if tot == 3:
			print "Winner is Player"
			exit()
		elif tot == 0:
			print "Winner is Computer "
			exit()

	tot1 = v,tot2 = v,tot3 = v
	t1 = 0,t2 = 0,t3 = 0
	for i in range(len(play)):
		for j in range(len(play)):
			if j == 0 :
				t1 = t1 + int(play[i][j])
			if j == 1 :
				t2 = t2 + int(play[i][j])
			if j == 2 :
				t3 = t3 + int(play[i][j])
	tot1 = t1,tot2 = t2,tot3 = t3
	if(tot1 == 3 or tot2 == 3 or tot3 == 3):
		print "Winner is Player"
		exit()
	elif(tot1 == 0 or tot2 == 0 or tot3 == 0):
		print "Winner is Computer"
		exit()

	if(play[0][0]+play[1][1]+play[2][2] == 3):
		print "Winner is Player"
		exit()
	elif(play[0][0]+play[1][1]+play[2][2] == 0):
		print "Winner is Computer"
		exit()
	if(play[0][2]+play[1][1]+play[2][0] == 3):
		print "Winner is Player"
		exit()
	elif(play[0][2]+play[1][1]+play[2][0] == 0):
		print "Winner is Computer"
		exit()

	if count == 9:
		print "Match Draw" 
		exit()
magic = np.array([[2,7,6],[9,5,1],[4,3,8]])
play = np.array([[-6,-6,-6],[-6,-6,-6],[-6,-6,-6]])
pos = []
comp = []
count = 0
v = -6
fir = int(raw_input("1 for Player moves first || 0 for Computer - "))
if fir == 1:
	switch = 3
	pmove()
elif fir == 0:
	switch = 4
	cmove()