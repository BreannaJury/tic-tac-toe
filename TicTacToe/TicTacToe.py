#playing board
board = {'A1': ' ', 'A2': ' ', 'A3': ' ',
		 'B1': ' ', 'B2': ' ', 'B3': ' ',
		 'C1': ' ', 'C2': ' ', 'C3': ' ',}

def printBoard():
	print('   1 2 3')
	print(' ')
	print('A  ' + board['A1'] + '|' + board['A2'] + '|' + board['A3'])
	print('   -+-+-')
	print('B  ' + board['B1'] + '|' + board['B2'] + '|' + board['B3'])
	print('   -+-+-')
	print('C  ' + board['C1'] + '|' + board['C2'] + '|' + board['C3'])

def play(player):
	pos=input("Make your turn: ")
	if pos in board:
		if board[pos] == ' ':
			#allowed input
			if player == 1:
				board[pos] = 'X'
			else:
				board[pos] = 'O'
		else:
			print("That space is already taken")
			play(player)
	else:
		print("That is not a valid position")
		play(player)

#size=input("Enter the size of the board (e.g. 3x3 = 3) (3-9) ")
player = 1
while True:
	printBoard()
	play(player)
	if player == 1:
		player = 2
	else:
		player = 1