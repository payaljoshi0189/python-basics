



def maxPathRecurse(grid, r, c):
	n = len(grid)
	m = len(grid[0])

	if r == n or c == m:
		return 0


	if r == n-1 and c == m-1:
		return grid[r][c]


	return grid[r][c] + max(maxPathRecurse(grid, r+1, c), maxPathRecurse(grid, r, c+1))


def maxPathMemoization(grid,table, r, c):
	n = len(grid)
	m = len(grid[0])

	if r == n or c == m:
		return 0

	if r == n - 1 and c == m - 1:
		if table[r][c] < -1:
			table[r][c] = grid[r][c]
		return table[r][c]
	
	row = maxPathRecurse(grid, r+1, c) if table[r+1][c] < 0 else table[r+1][c]
	col = maxPathRecurse(grid, r, c+1) if table[r][c+1] < 0 else table[r][c+1]

	table[r][c] = grid[r][c] + max(row, col)
	return table[r][c]





if __name__ == "__main__":
	grid = [[40, 60], [20, 50], [70, 100]]
	n = len(grid)
	m = len(grid[0])
	table = [[-1 for i in range(m)] for j in range(n)] 
	path = maxPathRecurse(grid, 0, 0)
	path1 = maxPathMemoization(grid, table, 0, 0)
	print("Recurse", path)
	print("Memoize", path1)

	





