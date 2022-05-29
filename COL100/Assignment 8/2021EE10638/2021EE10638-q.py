from typing import Tuple, List
# No other imports allowed

# PART OF THE DRIVER CODE

def input_sudoku():
	"""Function to take input a sudoku from stdin and return
	it as a list of lists.
	Each row of sudoku is one line.
	"""
	sudoku= list()
	for _ in range(9):
		row = list(map(int, input().rstrip(" ").split(" ")))
		sudoku.append(row)
	return sudoku

def print_sudoku(sudoku:List[List[int]]):
	"""Helper function to print sudoku to stdout
	Each row of sudoku in one line.
	"""
	for i in range(9):
		for j in range(9):
			print(sudoku[i][j], end = " ")
		print()

# You have to implement the functions below

def get_block_num(sudoku:List[List[int]], pos:Tuple[int, int]):
	"""This function takes a parameter position and returns
	the block number of the block which contains the position.
	"""
	return (((pos[0]-1)//3)*3)+((pos[1]-1)//3)+1

def get_position_inside_block(sudoku:List[List[int]], pos:Tuple[int, int]):
	"""This function takes parameter position
	and returns the index of the position inside the corresponding block.
	"""
	return (((pos[0]-1)%3)*3)+((pos[1]-1)%3)+1

def get_block(sudoku:List[List[int]], x: int):
	"""This function takes an integer argument x and then
	returns the x^th block of the Sudoku. Note that block indexing is
	from 1 to 9 and not 0-8.
	"""
	l=[]
	for i in range(3):
		l+=sudoku[((x-1)//3)*3:((x-1)//3)*3+3][i][((x-1)%3)*3:((x-1)%3)*3+3]
	return l

def get_row(sudoku:List[List[int]], i: int):
	"""This function takes an integer argument i and then returns
	the ith row. Row indexing have been shown above.
	"""
	return sudoku[i-1]

def get_column(sudoku:List[List[int]], x: int):
	"""This function takes an integer argument i and then
	returns the ith column. Column indexing have been shown above.
	"""
	l=[]
	for i in range(9):
		l.append(sudoku[i][x-1])
	return l

def find_first_unassigned_position(sudoku : List[List[int]]):
	"""This function returns the first empty position in the Sudoku. 
	If there are more than 1 position which is empty then position with lesser
	row number should be returned. If two empty positions have same row number then the position
	with less column number is to be returned. If the sudoku is completely filled then return `(-1, -1)`.
	"""
	for i in range(9):
		for j in range(9):
			if sudoku[i][j]==0:
				return (i+1,j+1)
	return (-1,-1)

def valid_list(lst: List[int]):
	"""This function takes a lists as an input and returns true if the given list is valid. 
	The list will be a single block , single row or single column only. 
	A valid list is defined as a list in which all non empty elements doesn't have a repeating element.
	"""
	l=[0]*10
	for i in lst:
		l[i]+=1
	for i in l[1:]:
		if i>1:
			return False
	return True

def valid_sudoku(sudoku:List[List[int]]):
	"""This function returns True if the whole Sudoku is valid.
	"""
	i=1
	while i<10 and valid_list(get_row(sudoku,i)) and valid_list(get_column(sudoku,i)) and valid_list(get_block(sudoku,i)):
		i+=1
	if i==10:
		return True
	return False

def get_candidates(sudoku:List[List[int]], pos:Tuple[int, int]):
	"""This function takes position as argument and returns a list of all the possible values that 
	can be assigned at that position so that the sudoku remains valid at that instant.
	"""
	l=[]
	for i in range(1,10):
		if i not in get_row(sudoku,pos[0]) and i not in get_column(sudoku,pos[1]) and i not in get_block(sudoku,get_block_num(sudoku,pos)):
			l.append(i)
	return l

def make_move(sudoku:List[List[int]], pos:Tuple[int, int], num:int):
	"""This function fill `num` at position `pos` in the sudoku and then returns
	the modified sudoku.
	"""	
	sudoku[pos[0]-1][pos[1]-1]=num
	return sudoku

def undo_move(sudoku:List[List[int]], pos:Tuple[int, int]):
	"""This function fills `0` at position `pos` in the sudoku and then returns
	the modified sudoku. In other words, it undoes any move that you 
	did on position `pos` in the sudoku.
	"""
	sudoku[pos[0]-1][pos[1]-1]=0
	return sudoku

def sudoku_solver(sudoku: List[List[int]]):
	""" This is the main Sudoku solver. This function solves the given incomplete Sudoku and returns 
	true as well as the solved sudoku if the Sudoku can be solved i.e. after filling all the empty positions the Sudoku remains valid.
	It return them in a tuple i.e. `(True, solved_sudoku)`.

	However, if the sudoku cannot be solved, it returns False and the same sudoku that given to solve i.e. `(False, original_sudoku)`
	"""
	a=find_first_unassigned_position(sudoku)
	while a!=(-1,-1):
		for i in get_candidates(sudoku,a):
			make_move(sudoku,a,i)
			if sudoku_solver(sudoku)[0]:return (True, sudoku)
			undo_move(sudoku,a)
		return(False,sudoku)
	return(True, sudoku)



# Following is the driver code
# you can edit the following code to check your performance.
if __name__ == "__main__":

	# Input the sudoku from stdin
	sudoku = input_sudoku()
	# Try to solve the sudoku
	if valid_sudoku(sudoku):
		possible, sudoku = sudoku_solver(sudoku)
		if possible:
			print("Found a valid solution for the given sudoku :)")
			print_sudoku(sudoku)
		else:
			print("The given sudoku cannot be solved :(")
			print_sudoku(sudoku)
	else:
		print("The given sudoku cannot be solved :(")
		print_sudoku(sudoku)