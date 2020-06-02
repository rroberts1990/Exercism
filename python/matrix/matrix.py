class Matrix:
    def __init__(self, matrix_string):
        self.rows = [list(map(int, i.split())) for i in matrix_string.split('\n')]
        self.columns = [list(col) for col in zip(*self.rows)]

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.columns[index-1]

