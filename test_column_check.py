from column_check import TwoColumnsImpliedThirdChecker
from sudoku_starter import SudokuBoard

def test_input():
	test = SudokuBoard()
	test.fill_board_from_list([[1,2,3,4,5,6,7,8,0],[2,0,0,0,0,0,0,0,0],[3,0,0,0,0,0,0,0,0],[4,1,0,0,0,0,0,0,0],[5,0,0,0,0,0,0,0,0],[6,0,2,0,0,0,0,0,0],[7,0,4,0,0,0,0,0,0],[8,0,0,0,0,0,0,0,0],[0,3,5,0,0,0,0,0,0]])
	test.print_board()
	filler = TwoColumnsImpliedThirdChecker()
	filler.test_columns(test)
	test.print_board()

test_input()