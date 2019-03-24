class SudokuBoard:

	def __init__(self):
		self.board = [[0 for i in range(9)] for j in range(9)]

	def fill_board_from_list(self,lines):
		for i in range(9):
			self.fill_line(i, lines[i])

	def fill_board(self):
		user_input = []
		for x in range(9):
			user_input.append(self.request_line(x))
			self.fill_line(x, user_input[x])

	def print_board(self):
		print("-----------------------------------")
		for y in range(9):
			for x in range(9):
				print(self.board[y][x],"| ", end = "")
			print("\n-----------------------------------")

	def fill_line(self, line_number, line_input):
		for x in range(9):
			self.board[line_number][x] = line_input[x]

	def request_line(self, line_number):
		print("Please enter line", line_number)
		line_info = input("->")
		line_input = line_info.split(" ")
		if self.line_syntax_correct(line_input):
			return list(map(int, line_input))
		else:
			print("Make sure to use the correct format")
			return request_line(line_number)

	def line_syntax_correct(self, numbers):
		if len(numbers) != 9:
			return False
		valid_numbers = [0,1,2,3,4,5,6,7,8,9]
		for number in numbers:
			if not int(number) in valid_numbers:
				return False
		return True
		#If we don't check that there aren't multiple of one number here we should check when puzzle is completely entered

	def check_space(self, row,column):
		return self.board[row][column]

	def set_space(self, row, column, number):
		self.board[row][column] = number

def main():
	print("Welcome to the Sudoku Solver")
	print("Enter each line of the given sudoku puzzle according to the following format:")
	print("A list of 9 integers where 0 represents a number that is not filled in")

	testBoard = SudokuBoard()
	testBoard.fill_board()
	testBoard.print_board()


if __name__ == '__main__':
	main()