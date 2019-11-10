from leezy import Solution, solution

from bisect import bisect_right, bisect_left
from itertools import chain

class Q074(Solution):
    @solution
    def searchMatrix(self, matrix, target):
        # O(m+n) 68ms 99.07% 
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False

    @solution
    def search_matrix(self, matrix, target):
        # 72ms 96.09%
        if not matrix or not matrix[0]:
            return False
        last_column = [row[-1] for row in matrix]
        row_idx = bisect_right(last_column, target)
        if row_idx > 0 and last_column[row_idx-1] == target:
            return True
        elif row_idx == len(matrix):
            return False
        row = matrix[row_idx]
        # idx = bisect_right(row, target)
        # return idx > 0 and row[idx-1] == target
        idx = bisect_left(row, target)
        return idx < len(row) and row[idx] == target

    @solution
    def search(self, matrix, target):
        # 144ms
        flat = list(chain.from_iterable(matrix))
        idx = bisect_left(flat, target)
        return idx < len(flat) and target == flat[idx]



def main():
    q = Q074()
    q.add_args([], 0)
    q.add_args([[1, 1]], 2)
    q.add_args([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3)
    q.add_args([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 7)
    q.add_args([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 50)
    q.add_args([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 13)
    q.run()


if __name__ == "__main__":
    main()
