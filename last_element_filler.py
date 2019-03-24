from sudoku_starter import SudokuBoard


class LastElementFiller:
	def check_for_eight_elements(self, board):
		for i in range(9):
			self.check_column(board,i)
			self.check_row(board, i)

	def check_column(self, board, column):
		num_elems = 0
		unfilled = 0 
		possible_nums = {1,2,3,4,5,6,7,8,9}
		for i in range(9):
			if board.check_space(i, column) != 0:
				num_elems += 1
				possible_nums.remove(board.check_space(i,column))
			else:
				unfilled = i
		if num_elems == 8:
			board.set_space(i, column, possible_nums.pop())	

	def check_row(self, board, row):
		num_elems = 0
		unfilled = 0 
		possible_nums = {1,2,3,4,5,6,7,8,9}
		for i in range(9):
			if board.check_space(row, i) != 0:
				num_elems += 1
				possible_nums.remove(board.check_space(row, i))
			else:
				unfilled = i
		if num_elems == 8:
			board.set_space(row, i, possible_nums.pop())
