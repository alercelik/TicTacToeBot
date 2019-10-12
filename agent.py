# Agent

BOARD_SIZE = 3


import random
from game import check_finish, print_board


chars = ["X", "O"]

class TicTacToeAgent:
	"""
	Her elde tree'yi oluştur veya sadece ilk turn'de oluştur
	"""
	def __init__(self, board, whose_turn):
		self.whose_turn = whose_turn
		self.agents_turn = whose_turn
		self.char = chars[whose_turn-1]

		self.board = board[:]

		self.update_tree_each_turn = True
		self.tree = None
		self.use_tree = True

		print("Agent created")

	def play_randomly(self, board):
		empty_cells = [(i, j) for i in range(BOARD_SIZE) for j in range(BOARD_SIZE) if board[i][j] == "."]

		choice = random.choice(empty_cells)
		return choice

	def play(self, board):
		if self.use_tree:
			if self.update_tree_each_turn:
				self.tree = self.construct_tree(board[:])
			else:
				if self.tree is None:
					self.tree = self.construct_tree(board[:])

			return self.tree.backward()
		else:
			return self.play_randomly(board[:])


	def construct_tree(self, board):
		return Tree(board[:], self.whose_turn, is_agents_turn=True)


class Tree:
	def __init__(self, board, turn_counter, is_agents_turn):
		self.whose_turn = 2 - (turn_counter%2)
		self.turn_counter = turn_counter

		self.char = chars[self.whose_turn-1]

		self.remaining_moves = (BOARD_SIZE**2 +1) - turn_counter

		self.root = TreeNode(board[:], self.whose_turn, self.char)

	def backward(self):
		print("backwarding..")
		# root asks his children for their points and takes maximum

		return self.root.get_action()


class TreeNode:
	def __init__(self, board, whose_turn, agents_char):
		self.board = board[:]

		#print_board(self.board)

		self.whose_turn = whose_turn

		self.score = None

		winner = check_finish(self.board)

		if winner == -1: # no winner yet
			self.possible_actions = [(i, j) for i in range(BOARD_SIZE) for j in range(BOARD_SIZE) if self.board[i][j] == "."]

			#print("There are {} possible moves here".format(len(self.possible_actions)))

			self.children = []
			for counter, (i, j) in enumerate(self.possible_actions):
				#print("Creating {}. node {},{}".format(counter, i, j))
				#print("self board is:")
				#print_board(self.board)

				new_board = self.board[:]
				new_board[i][j] = chars[whose_turn-1]


				#print("self board after new_board move is:")
				#print_board(self.board)


				self.children.append(
					TreeNode(new_board[:], 3-whose_turn, agents_char)
				)

				self.board[i][j] = "." # backtracking

		elif winner == 0:
			self.score = 0
			#print("here is a draw")
		elif winner == agents_char:
			self.score = 1
			#print("agent wins here")
		else:
			self.score = -1
			#print("you win here")



	def get_action(self):
		"""
		only the root node calls this function
		returns the best action (i,j)
		"""
		scores = [child.get_score(False) for child in self.children]

		max_score = max(scores)
		max_index = scores.index(max_score)
		self.score = max_score

		best_action = self.possible_actions[max_index]
		return best_action


	def get_score(self, is_agents_turn):
		"""
		returns the score, if not exist, asks children and gets the max recursively
		"""

		if self.score is None:
			# start recursion
			scores = [child.get_score(not(is_agents_turn)) for child in self.children]

			if is_agents_turn:
				self.score = max(scores)
			#total_score = sum(scores)
			#max_score = max(scores)
			#max_index = scores.index(max_score)
			else:
				self.score = min(scores)

		#print("My score is {} and my table is".format(self.total_score))

		return self.score





		
