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
	pos=input("Make your turn player "+player+": ")
	if pos in board:
		if board[pos] == ' ':
			#allowed input
			if player == "1":
				board[pos] = 'X'
			else:
				board[pos] = 'O'
		else:
			print("That space is already taken")
			play(player)
	else:
		print("That is not a valid position")
		play(player)

def checkWinner(player, count):
	#horizontals
	if board['A1'] == board['A2'] == board['A3'] != ' ':
		print("Player " + player + " is the winner!")
	elif board['B1'] == board['B2'] == board['B3'] != ' ':
		print("Player " + player + " is the winner!")
	elif board['C1'] == board['C2'] == board['C3'] != ' ':
		print("Player " + player + " is the winner!")
	#verticals
	elif board['A1'] == board['B1'] == board['C1'] != ' ':
		print("Player " + player + " is the winner!")
	elif board['A2'] == board['B2'] == board['C2'] != ' ':
		print("Player " + player + " is the winner!")
	elif board['A3'] == board['B3'] == board['C3'] != ' ':
		print("Player " + player + " is the winner!")
	#diagonals
	elif board['A1'] == board['B2'] == board['C3'] != ' ':
		print("Player " + player + " is the winner!")
	elif board['A3'] == board['B2'] == board['C1'] != ' ':
		print("Player " + player + " is the winner!")
	#tie
	elif count == 9:
		print("You have tied")
	#no winner yet
	else:
		start(player, count)

def start(player, count):
	printBoard()
	play(player)
	count = count + 1
	if player == "1":
		player = "2"
	else:
		player = "1"
	checkWinner(player, count)


#size=input("Enter the size of the board (e.g. 3x3 = 3) (3-9) ")
player = "1"
count = 0
start(player, count)