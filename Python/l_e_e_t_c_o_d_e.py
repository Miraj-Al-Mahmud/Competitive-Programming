# @copyright BOOGEYMAN
# LEETCODE simplifier V3




def main() -> None:
	
	

	"""
	board = [["5","3",".",".","7",".",".",".","."]
	,["6",".",".","1","9","5",".",".","."]
	,[".","9","8",".",".",".",".","6","."]
	,["8",".",".",".","6",".",".",".","3"]
	,["4",".",".","8",".","3",".",".","1"]
	,["7",".",".",".","2",".",".",".","6"]
	,[".","6",".",".",".",".","2","8","."]
	,[".",".",".","4","1","9",".",".","5"]
	,[".",".",".",".","8",".",".","7","9"]]
	"""


	board = [["8","3",".",".","7",".",".",".","."]
	,["6",".",".","1","9","5",".",".","."]
	,[".","9","8",".",".",".",".","6","."]
	,["8",".",".",".","6",".",".",".","3"]
	,["4",".",".","8",".","3",".",".","1"]
	,["7",".",".",".","2",".",".",".","6"]
	,[".","6",".",".",".",".","2","8","."]
	,[".",".",".","4","1","9",".",".","5"]
	,[".",".",".",".","8",".",".","7","9"]]



	flag = False
	def row(l):
		flag = False
		store = [0]*10
		for i in l:
			if i!='.': store[int(i)]+=1
		for i in store:
			if i>1: flag = True; break
		return flag # false if everything is okay

	for b in board:
		if row(b) == True: return False
	
	for i in range(0,9):
		l = []
		for j in board: l.append(j[i])
		if row(l) == True: return False

	idx = 0
	for j in range(0,9,3):
		l = []
		temp = idx
		for ll in range(3):
			for cc in range(3): # for rows
				l.append(board[temp+c+ll][0],board[temp+c+ll][1],board[temp+c+ll][2])
			if row(l) == True: return False
			l.clear()
			temp+=1

		idx+=1
	return True




	


	
		
	
	
			
			
		
		



if __name__ == '__main__':
	import baba_yaga
	from baba_yaga import L
	
	raincheck = main()
	if raincheck == False: print(f"false",end="\n")
	elif raincheck == True: print(f"true",end="\n")
	elif raincheck==None: print(f"<-< No value to return >->",end="\n")
	else: print(f'{raincheck}',end="\n")
	
	baba_yaga._generator_()







