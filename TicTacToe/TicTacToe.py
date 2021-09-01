#playing board
#board[][] = new char[][]
#board = {'A1': ' ', 'A2': ' ', 'A3': ' ',
#		 'B1': ' ', 'B2': ' ', 'B3': ' ',
#		 'C1': ' ', 'C2': ' ', 'C3': ' ',}

#boardList = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

def printBoard(size, board):
	for i in range (size):
		for j in range (size-1):
			print(board[i][j], end = "|")
		print(board[i][size-1])
		if i != size-1:
			for k in range(size):
				print("--", end = "")
			print()

def play(player, size):
	print("Make your turn "+player+": ")
	rowInput = int(input("Row: (0 - "+size-1+") "))
	colInput = int(input("Column: (0 - "+size-1+") "))
	#if pos in board:
	if board[rowInput][colInput] == ' ':
			#allowed input
	#	boardList.remove(pos)
		if player == "Player 1":
			board[rowInput][colInput] = 'X'
		else:
			board[rowInput][colInput] = 'O'
	else:
	#	print("That space is already taken")
		print("You cannot play there")
		play(player, size)
	#else:
	#	print("That is not a valid position")
	#	play(player)

def computer(size, board):
	import random
	valid=True
	while valid:
		rowRand = random.randint(0, size)
		colRand = random.randint(0, size)
		if board[rowRand][colRand] == ' ':
			board[rowRand][colRand] = 'O'
			valid=False
	#pos = boardList[r]
	print("The computer played "+ rowRand + ", " + colRand)
	#board[pos] = 'O'
	#boardList.remove(pos)

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


print("Welcome to Tic Tac Toe")
#get game type
valid=True
while valid:
	gType = input("Would you like to play against a friend or the computer? (Enter f or c) ")
	if gType == "f":		
		valid=False
	elif gType == "c":
		valid=False
	else:
		print("Please enter a valid input")
		
#get board size
valid=True
while valid:
	size=int(input("Enter the size of the board (e.g. 3x3 = 3) (3-9) "))
	if size < 3:
		print("That is too small")
	elif size > 9:
		print("That is too large")
	else:
		valid=False

#build board
rows,cols = (size, size)
board = [[0 for i in range(cols)] for j in range(rows)]
for i in range(rows):
	for j in range(cols):
		board[i][j] = ' '

player = "Player 1"
count = 0
printBoard(size, board)
#start(player, count, gType)
#game(player, count)
