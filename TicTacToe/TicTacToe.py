#playing board
board = {'A1': ' ', 'A2': ' ', 'A3': ' ',
		 'B1': ' ', 'B2': ' ', 'B3': ' ',
		 'C1': ' ', 'C2': ' ', 'C3': ' ',}

boardList = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

def printBoard():
	print('   1 2 3')
	print(' ')
	print('A  ' + board['A1'] + '|' + board['A2'] + '|' + board['A3'])
	print('   -+-+-')
	print('B  ' + board['B1'] + '|' + board['B2'] + '|' + board['B3'])
	print('   -+-+-')
	print('C  ' + board['C1'] + '|' + board['C2'] + '|' + board['C3'])

def play(player):
	pos=input("Make your turn "+player+": ")
	if pos in board:
		if board[pos] == ' ':
			#allowed input
			boardList.remove(pos)
			if player == "Player 1":
				board[pos] = 'X'
			else:
				board[pos] = 'O'
		else:
			print("That space is already taken")
			play(player)
	else:
		print("That is not a valid position")
		play(player)

def computer():
	import random
	r = random.randint(0, len(boardList))
	pos = boardList[r]
	print("The computer played "+pos)
	board[pos] = 'O'
	boardList.remove(pos)

def winner(player, gameType):
	printBoard()
	if gameType == "c":
		if player == "Player 1":
			print("The computer is the winner :(")
		else:
			print("You win!")
	else:
		if player == "Player 1":
			print("Player 2 is the winner!")
		else:
			print("Player 1 is the winner!")

def checkWinner(player, count, gameType):
	#horizontals
	if board['A1'] == board['A2'] == board['A3'] != ' ':
		winner(player, gameType)
	elif board['B1'] == board['B2'] == board['B3'] != ' ':
		winner(player, gameType)
	elif board['C1'] == board['C2'] == board['C3'] != ' ':
		winner(player, gameType)
	#verticals
	elif board['A1'] == board['B1'] == board['C1'] != ' ':
		winner(player, gameType)
	elif board['A2'] == board['B2'] == board['C2'] != ' ':
		winner(player, gameType)
	elif board['A3'] == board['B3'] == board['C3'] != ' ':
		winner(player, gameType)
	#diagonals
	elif board['A1'] == board['B2'] == board['C3'] != ' ':
		winner(player, gameType)
	elif board['A3'] == board['B2'] == board['C1'] != ' ':
		winner(player, gameType)
	#tie
	elif count == 9:
		print("You have tied")
	#no winner yet
	else:
		start(player, count, gameType)

def start(player, count, gameType):
	printBoard()
	#2 player
	if gameType == "f":
		play(player)
		if player == "Player 1":
			player = "Player 2"
		else:
			player = "Player 1"
	#1 player vs computer
	else:
		if player == "Player 1":
			play(player)
			player = "The computer"
		else:
			computer()
			player = "Player 1"
	count = count + 1
	checkWinner(player, count, gameType)


def game(player, count):
	gType = input("Would you like to play against a friend or the computer? (Enter f or c) ")
	if gType == "f":
		start(player, count, gType)
	elif gType == "c":
		start(player, count, gType)
	else:
		print("Please enter a valid input")
		game(player, count)


#size=input("Enter the size of the board (e.g. 3x3 = 3) (3-9) ")
player = "Player 1"
count = 0
print("Welcome to Tic Tac Toe")

game(player, count)
