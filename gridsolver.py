"""
Solve the following problem:
x 1 4 5 9
2 3 9 8 3
1 3 2 4 2
2 7 7 6 y
Starting from x and only going either right or down, find the path with the highest sum of numbers
(given any grid of size m*n)
"""
import np
test = [
	[0, 3, 4],
	[2, 5, 6],
	[1, 3, 0]
]


def gridsolve(grid):
	subsections = np.full(grid.shape, -1)
	def recursiveSolve(i,j,grid):
		if subsections[i,j] != -1:
			return subsections[i,j]
		elif subsections[i,j]