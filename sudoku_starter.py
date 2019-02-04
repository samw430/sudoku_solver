def main():
	print("Welcome to the Sudoku Solver")
	print("Enter each line of the given sudoku puzzle according to the following format:")
	print("A list of 9 integers where 0 represents a number that is not filled in")

	line0 = request_line(0)
	line1 = request_line(1)
	line2 = request_line(2)
	line3 = request_line(3)
	line4 = request_line(4)
	line5 = request_line(5)
	line6 = request_line(6)
	line7 = request_line(7)
	line8 = request_line(8)

	sudoku_board = [[0 for x in range(9)] for y in range(9)]
	sudoku_board = fill_line(sudoku_board, 0, line0)
	sudoku_board = fill_line(sudoku_board, 1, line1)
	sudoku_board = fill_line(sudoku_board, 2, line2)
	sudoku_board = fill_line(sudoku_board, 3, line3)
	sudoku_board = fill_line(sudoku_board, 4, line4)
	sudoku_board = fill_line(sudoku_board, 5, line5)
	sudoku_board = fill_line(sudoku_board, 6, line6)
	sudoku_board = fill_line(sudoku_board, 7, line7)
	sudoku_board = fill_line(sudoku_board, 8, line8)

	print_board(sudoku_board)

def print_board(sudoku_board):
	print("-----------------------------------")
	for y in range(9):
		print(sudoku_board[y][0],"|",sudoku_board[y][1],"|",sudoku_board[y][2],"|",sudoku_board[y][3],"|",sudoku_board[y][4],"|",sudoku_board[y][5],"|",sudoku_board[y][6],"|",sudoku_board[y][7],"|",sudoku_board[y][8],"|")
		print("-----------------------------------")

def fill_line(sudoku_board, line_number, line_input):
	for x in range(9):
		sudoku_board[line_number][x] = line_input[x]
	return sudoku_board

def request_line(line_number):
	print("Please enter line", line_number)
	line_info = input("->")
	line_input = line_info.split(" ")
	if line_syntax_correct(line_input):
		return list(map(int, line_input))
	else:
		print("Make sure to use the correct format")
		request_line(line_number)

def line_syntax_correct(numbers):
	if len(numbers) != 9:
		return False
	valid_numbers = [0,1,2,3,4,5,6,7,8,9]
	for number in numbers:
		if not int(number) in valid_numbers:
			return False
	return True
	#If we don't check that there aren't multiple of one number here we should check when puzzle is completely entered

if __name__ == '__main__':
	main()