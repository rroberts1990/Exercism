def saddle_points(matrix):
	if is_matrix_invalid(matrix):
		raise ValueError("The supplied matrix is invalid.")
	else:
		rows = matrix
		columns = transpose_matrix(matrix)
		saddlepoints = []
		for rownum, row in enumerate(rows):
			for colnum, num in enumerate(row):
				if max(rows[rownum]) == min(columns[colnum]):
					saddlepoints.append({"row": rownum+1, "column": colnum+1})
		return saddlepoints

def is_matrix_invalid(matrix):
    return any(len(row) != len(matrix[0]) for row in matrix)

def transpose_matrix(matrix):
	return [list(column) for column in zip(*matrix)]




