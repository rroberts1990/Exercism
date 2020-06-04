from typing import List

class Matrix:
    def __init__(self, matrix_string: str):
        self.rows = [list(map(int, i.split())) for i in matrix_string.split('\n')]

    def row(self, index: int) -> List[int]:
        return self.rows[index-1]

    def column(self, index: int) -> List[int]:
        return [row[index-1] for row in self.rows]



