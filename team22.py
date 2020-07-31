import numpy as np
class Team22:
	'''player of team 22'''
	def __init__(self):
		'''maxm depth searched is 4'''
		self.depth = 4

	def utility(self,smallboard,flag):
		uty = 0
		sb = np.array(smallboard)
		D1 = np.diag(smallboard) 
		D2 = np.diag(smallboard[::-1])[::-1]
		#utility for single flag
		A = [flag,' ',' ']
		B = [' ',flag,' ']
		C = [' ',' ',flag]
		D = [' ',' ',' ']
		for row in sb:
			if np.array_equal(A,row) or np.array_equal(B,row) or np.array_equal(C,row):
				uty = uty + 1

		for i in range(0,3):
			D = sb[:,i]
			if np.array_equal(A,D) or np.array_equal(B,D) or np.array_equal(C,D):
				uty = uty + 1
		
		if np.array_equal(A,D1) or np.array_equal(B,D1) or np.array_equal(C,D1):
			uty = uty + 1
		if np.array_equal(A,D2) or np.array_equal(B,D2) or np.array_equal(C,D2):
			uty = uty + 1
		
		#2 flags
		A = [flag,flag,' ']
		B = [flag,' ',flag]
		C = [' ',flag,flag]
		for row in sb:
			if np.array_equal(A,row) or np.array_equal(B,row) or np.array_equal(C,row):
				uty = uty + 10

		for i in range(0,3):
			D = sb[:,i]
			if np.array_equal(A,D) or np.array_equal(B,D) or np.array_equal(C,D):
				uty = uty + 10
		
		if np.array_equal(A,D1) or np.array_equal(B,D1) or np.array_equal(C,D1):
			uty = uty + 10
		if np.array_equal(A,D2) or np.array_equal(B,D2) or np.array_equal(C,D2):
			uty = uty + 10

		#3 flags
		A = [flag,flag,flag]
		for row in sb:
			if np.array_equal(A,row):
				uty = uty + 100

		for i in range(0,3):
			D = sb[:,i]
			if np.array_equal(A,D):
				uty = uty + 100
		
		if np.array_equal(A,D1):
			uty = uty + 100
		if np.array_equal(A,D2):
			uty = uty + 100
		if flag == 'x':
			flag1 = 'o'
		else:
			flag1 = 'x'
		#single flag
		A = [flag1,' ',' ']
		B = [' ',flag1,' ']
		C = [' ',' ',flag1]
		D = [' ',' ',' ']
		for row in sb:
			if np.array_equal(A,row) or np.array_equal(B,row) or np.array_equal(C,row):
				uty = uty - 1

		for i in range(0,3):
			D = sb[:,i]
			if np.array_equal(A,D) or np.array_equal(B,D) or np.array_equal(C,D):
				uty = uty - 1
		
		if np.array_equal(A,D1) or np.array_equal(B,D1) or np.array_equal(C,D1):
			uty = uty - 1
		if np.array_equal(A,D2) or np.array_equal(B,D2) or np.array_equal(C,D2):
			uty = uty - 1
		
		#2 flags
		A = [flag1,flag1,' ']
		B = [flag1,' ',flag1]
		C = [' ',flag1,flag1]
		for row in sb:
			if np.array_equal(A,row) or np.array_equal(B,row) or np.array_equal(C,row):
				uty = uty - 10

		for i in range(0,3):
			D = sb[:,i]
			if np.array_equal(A,D) or np.array_equal(B,D) or np.array_equal(C,D):
				uty = uty - 10
		
		if np.array_equal(A,D1) or np.array_equal(B,D1) or np.array_equal(C,D1):
			uty = uty - 10
		if np.array_equal(A,D2) or np.array_equal(B,D2) or np.array_equal(C,D2):
			uty = uty - 10

		#3 flags
		A = [flag1,flag1,flag1]
		for row in sb:
			if np.array_equal(A,row):
				uty = uty - 100

		for i in range(0,3):
			D = sb[:,i]
			if np.array_equal(A,D):
				uty = uty - 100
		
		if np.array_equal(A,D1):
			uty = uty - 100
		if np.array_equal(A,D2):
			uty = uty - 100
		return uty

	def alpha_beta_minimax(self,node,alpha,beta,isMaxPlayer,depth,flag,flag1,board_no,sb_no):
		mat = node
		best = [board_no,sb_no,-1,-100000]
		if depth==self.depth:
			out = [board_no,sb_no,-1,self.utility(node,flag)]
			return out
		else:
			# max player
			if isMaxPlayer:
				for i in range(0,3):
					for j in range(0,3):
						mat = node
						if mat[i][j]=='-':
							mat[i][j]=flag
							value = self.alpha_beta_minimax(mat,alpha,beta,False,depth+1,flag,flag1,board_no,sb_no)
							if value[3] >= best[3]:
								best[3] = value[3]
								best[2]=(i*3)+j
							if alpha >= best[3]:
								alpha = best[3]
							if beta <= alpha:
								break
				return best
			# min player turn
			else:
				best[3] = 100000
				for i in range(0,3):
					for j in range(0,3):
						if mat[i][j]=='-':
							mat = node
							mat[i][j]=flag1
							value = self.alpha_beta_minimax(mat,alpha,beta,True,depth+1,flag,flag1,board_no,sb_no)
							if value[3] <= best[3]:
								best[3] = value[3]
								best[2]=(i*3)+j
							if beta <= best[3]:
								beta = best[3]
							if beta <= alpha:
								break
				return best

	def move(self, board, old_move, flag):
		#utility initialize
		max_utility = 0
		b = 1
		if flag == 'x':
			flag1 = 'o'
		else:
			flag1 = 'x'
		smallboards=[]
		#valid possible cells
		cells = board.find_valid_move_cells(old_move)
		#if initial player 
		if len(cells)==162:
			return (0,3,5)
			# get small boards of cells
		for cell in cells:
			cell_board = cell[0]
			cell_smallboard = ((cell[1]/3)*3 + cell[2]/3)
			row_sb = (cell_smallboard/3)*3
			col_sb = (cell_smallboard%3)*3
			sba = [board.big_boards_status[cell_board][row_sb][col_sb:(col_sb+3)]]
			sba.append(board.big_boards_status[cell_board][(row_sb+1)][(col_sb):(col_sb+3)])
			sba.append(board.big_boards_status[cell_board][row_sb+2][col_sb:(col_sb+3)])
			sba.append([cell_board,cell_smallboard])
			if len(smallboards)==0:
				smallboards.append(sba)
			else:
				b = 1
				for M in smallboards:
					if M[3][0]==cell_board and M[3][1]==cell_smallboard:
						b = 0
						break
				if b==1:
					smallboards.append(sba)
		output  = [0,0,0,0]
		output1 = [0,0,0,0]
		output2 = [0,0,0,0]
		#one valid possible small board
		if len(smallboards)==1:
			output = self.alpha_beta_minimax(smallboards[0][0:3],-100000,100000,True,0,flag,flag1,smallboards[0][3][0],smallboards[0][3][1])
		# two valid possible small boards
		if len(smallboards)==2:
			output1 = self.alpha_beta_minimax(smallboards[0][0:3],-100000,100000,True,0,flag,flag1,smallboards[0][3][0],smallboards[0][3][1])
			output2 = self.alpha_beta_minimax(smallboards[1][0:3],-100000,100000,True,0,flag,flag1,smallboards[1][3][0],smallboards[1][3][1])
			if output2[3] > output1[3]:
				output = output2
			else:
				output = output1
		# more than 2 small boards present
		if len(smallboards)>2:
			max_utility = -1000000
			u = 0
			index = 0
			for i in range(0,len(smallboards)):
				u = self.utility(smallboards[i][0:3],flag)
				if u>=max_utility:
					max_utility = u
					index = i
			output = self.alpha_beta_minimax(smallboards[index][0:3],-10000,10000,True,0,flag,flag1,smallboards[index][3][0],smallboards[index][3][1])
		row = (output[1]/3)*3 + output[2]/3
		column = (output[1]%3)*3 + output[2]%3
		return (output[0],row,column) 