from leeyzer import Solution, solution


class Q074(Solution):
    @solution
    def searchMatrix(self, matrix, target):
        # O(m+n) 40ms 95.85% 
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


def main():
    q = Q074()
    q.add_args([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3)
    q.add_args([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 13)
    q.run()


if __name__ == "__main__":
    main()
