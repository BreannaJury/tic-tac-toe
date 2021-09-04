#player = "Player 1"
#gameType = "f"
#size = 0
#count = 0
#rowPos = 0
#colPos = 0

def printBoard(size, board):
	for i in range (size):
		for j in range (size-1):
			print(board[i][j], end = "|")
		print(board[i][size-1])
		if i != size-1:
			for k in range(size):
				print("--", end = "")
			print()

def play(player, size, board, count, gameType): 
	count = count + 1
	print("Make your turn "+player+": ")
	validRange = str(size - 1)
	rowPos = int(input("Row: (0 - "+validRange+"): "))
	colPos = int(input("Column: (0 - "+validRange+"): "))
	if board[rowPos][colPos] == ' ':
			#allowed input
		if player == "Player 1":
			board[rowPos][colPos] = 'X'
		else:
			board[rowPos][colPos] = 'O'
		checkWinner(player, count, gameType, board, rowPos, colPos)
	else:
		print("You cannot play there")
		play(player, size, board)


def computer(size, board, player, count, gameType):
	count = count + 1
	import random
	valid=True
	while valid:
		rowPos = random.randint(0, size)
		colPos = random.randint(0, size)
		if board[rowPos][colPos] == ' ':
			board[rowPos][colPos] = 'O'
			valid=False
	print("The computer played "+ rowPos + ", " + colPos)
	checkWinner(player, count, gameType, board, rowPos, colPos)

def winner(player, gameType, board): 
	printBoard(size, board)
	print("check2")
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

def checkWinner(player, count, gameType, board, rowPos, colPos):
	#row
	win = True
	for i in range(size-1):
		if board[rowPos][i] != board[rowPos][i+1]:
			win = False
	if win:
		print("check1")
		winner(player, gameType, board)

	#col
	win = True
	for i in range(size-1):
		if board[i][colPos] != board[i+1][colPos]:
			win = False
	if win:
		winner(player, gameType, board)

	#forward diagonal
	if rowPos == colPos:
		win = True
		for i in range(size-1):
			if board[i][i] != board[i+1][i+1]:
				win = False
		if win:
			winner(player, gameType, board)

	#back diagonal
	if rowPos + colPos == size-1:
		win = True
		for i in range(size-1):
			if board[i][size-1-i] != board[i+1][size-2-i]:
				win = False
		if win:
			winner(player, gameType, board)

	elif count == size*size:
		print("You have tied")

	else:
		start(player, count, gameType, size, board)


def start(player, count, gameType, size, board): 
	printBoard(size, board)
	#2 player
	if gameType == "f":
		if player == "Player 1":
			player = "Player 2"
			play(player, size, board, count, gameType)
		else:
			player = "Player 1"
			play(player, size, board, count, gameType)
	#1 player vs computer
	else:
		if player == "Player 1":

			player = "The computer"
			computer(size, board, player, count, gameType)
		else:
			player = "Player 1"
			play(player, size, board, count, gameType)


print("Welcome to Tic Tac Toe")
#get game type
valid=True
while valid:
	gameType = input("Would you like to play against a friend or the computer? (Enter f or c) ")
	if gameType == 'f':		
		valid=False
	elif gameType == 'c':
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

count = 0
player = 'Player 1'
printBoard(size, board)
play(player, size, board, count, gameType)
#start(player, count, gameType, size, board)

