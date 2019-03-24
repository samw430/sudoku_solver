from sudoku_starter import SudokuBoard

class TwoColumnsImpliedThirdChecker:
#Goal: Given two columns that have the number, check whether third column implies location

	def test_columns(self, board):
		for i in range(9):
			for base_column in range(3):
				self.test_triple(board, base_column, i)

	def test_triple(self, board, base_column, desired_number):
		locations = []
		for i in range(3):
			for j in range(9):
				if board.check_space(j, base_column+i) == desired_number:
					locations.append((j, base_column+i))
		if len(locations) == 2:
			possible_columns = {base_column, base_column+1, base_column+2}
			possible_blocks = {0, 1, 2}

			for (row, column) in locations:
				possible_columns.remove(column)
				possible_blocks.remove(row//3)

			column = possible_columns.pop()
			quadrant = possible_blocks.pop()*3

			possible_rows = {quadrant, quadrant+1, quadrant+2}
			valid_rows = [quadrant, quadrant+1, quadrant+2]

			for row in possible_rows:
				for i in range(9):
					if board.check_space(row,i) == desired_number:
						valid_rows.remove(row)
				if row in valid_rows and board.check_space(row, column) != 0:
					valid_rows.remove(row)
			if len(valid_rows) == 1:
				board.set_space(valid_rows.pop(), column, desired_number)