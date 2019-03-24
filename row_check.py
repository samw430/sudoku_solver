from sudoku_starter import SudokuBoard

class RowChecker:
#Goal: Given two columns that have the number, check whether third column implies location

	def test_rows(self, board):
		for i in range(9):
			for base_row in range(3):
				self.test_triple(board, base_row, i)

	def test_triple(self, board, base_row, desired_number):
		locations = []
		for i in range(3):
			for j in range(9):
				if board.check_space(base_row+i, j) == desired_number:
					locations.append((base_row+i, j))
		if len(locations) == 2:
			possible_rows = {base_row, base_row+1, base_row+2}
			possible_blocks = [0, 1, 2]

			for (row, column) in locations:
				possible_rows.remove(row)
				possible_blocks.remove(column//3)


			row = possible_rows.pop()
			quadrant = possible_blocks.pop()*3

			print(row)
			print(quadrant)

			possible_columns = {quadrant, quadrant+1, quadrant+2}
			valid_columns = [quadrant, quadrant+1, quadrant+2]

			for column in possible_columns:
				for i in range(9):
					if board.check_space(i, column) == desired_number:
						valid_columns.remove(column)
				if column in valid_columns and board.check_space(row, column) != 0:
					valid_columns.remove(column)
			if len(valid_columns) == 1:
				board.set_space(row, valid_columns.pop(),desired_number)