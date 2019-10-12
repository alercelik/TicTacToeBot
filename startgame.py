BOARD_SIZE = 3
chars = ["X", "O"]


from game import *
from agent import TicTacToeAgent

def start_game():
	board = [["." for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]

	start_choice = int(input("Who starts?\n1- You\n2- Computer\n: "))

	agent_start_turn = 3 - start_choice
	agent = TicTacToeAgent(board, agent_start_turn)

	whose_turn = 1
	turn_counter = 1


	while True:

		print("Player {}'s turn ({})".format(whose_turn, chars[whose_turn-1]))
		print_board(board)

		if whose_turn == start_choice:
			i = int(input("Enter row-1: "))
			j = int(input("Enter column-1: "))
		else:
			i, j = agent.play(board)

			print("computer plays {},{}".format(i,j))

		print()

		board[i][j] = chars[whose_turn-1]

		# check if game is over
		winner = check_finish(board[:])
		if winner == -1:
			pass
		elif winner == 0:
				print("draw")
				break
		else:
			print("Player {} wins!".format(whose_turn))
			break

		whose_turn = 3 - whose_turn
		turn_counter += 1

	print("GAME ENDED")
	print_board(board)


if __name__ == '__main__':
	start_game()
