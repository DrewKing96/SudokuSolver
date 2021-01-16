board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#Solve the sudoku puzzle
def solve(board):
	newEmpty = getEmpty(board)
	#no empty slots left in board
	if not newEmpty:
		return True
	else:
		(row, col) = newEmpty
	for num in range(1, 10):
		if(validate(board, num, (row, col))):
			board[row][col] = num
			if(solve(board)):
				return True
			board[row][col] = 0
	return False;

#grab the next empty slot in puzzle
def getEmpty(board):
	#iterating through sudoku board for next empty slot
	for row in range(len(board)):
		for col in range(len(board[0])):
			if(board[row][col] == 0):
				#returning row and col indexes for found empty slot
				return (row, col)
	return None

#verify number in the current location row
def checkRow(board, num, currLoc):
	for i in range(len(board[0])):
		if(board[currLoc[0]][i] == num and currLoc[1] != i):
			return False
	return True

#verify number in the current location col
def checkCol(board, num, currLoc):
	for i in range(len(board)):
		if(board[i][currLoc[1]] == num and currLoc[0] != i):
			return False
	return True	

#verify number in the current location square
def checkSquare(board, num, currLoc):
	square_x = currLoc[1] // 3
	square_y = currLoc[0] // 3

	for i in range(square_y*3, ((square_y*3)+3)):
		for j in range(square_x*3, ((square_x*3)+3)):
			if(board[i][j] == num and (i,j) != currLoc):
				return False
	return True

#validate number being placed in the current location
def validate(board, num, currLoc):
	return(checkRow(board, num, currLoc) and checkCol(board, num, currLoc) and checkSquare(board, num, currLoc))


#show sudoku board
def display(board):
	x = 1
	print("________________________")
	for row in range(len(board)):
		for col in range(len(board[0])):
			if(col%3 == 0):
				print('|', end =" ")
			if(col == 8):
				print(str(board[row][col]) + '|')
				if(x%3 == 0 and x!=9):
					print("|======================|")
				x = x+1
			else:
				print(board[row][col], end =" ")
	print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

display(board)
solve(board)
display(board)