BOARD_SIZE = 3
chars = ["X", "O"]


def print_board(board):
	print("__Board__")
	for line in board:
		print("|", end="")
		for col in line:
			print(" {}".format(col), end="")
		print(" |")


def check_finish(board):
	"""
	"X" -> X wins
	"O" -> O wins
	0 -> draw
	-1 -> not finished
	"""
	for c in ["X", "O"]:
		# check rows
		for i in range(BOARD_SIZE):
			for j in range(BOARD_SIZE):
				if board[i][j] == c:
					continue
				else:
					break
			else:
				return c


		# check columns
		for j in range(BOARD_SIZE):
			for i in range(BOARD_SIZE):
				if board[i][j] == c:
					continue
				else:
					break
			else:
				return c

		# check diagonals
		for i in range(BOARD_SIZE):
			if board[i][i] == c:
				continue
			else:
				break
		else:
			return c

		for i in range(BOARD_SIZE):
			if board[i][(BOARD_SIZE-1)-i] == c:
				continue
			else:
				break
		else:
			return c

	
	possible_move_count = sum(row.count(".") for row in board)
	if possible_move_count == 0:
		return 0
	else:
		return -1


