from leezy import solution, Solution

class Q240(Solution):
    @solution
    def searchMatrix(self, matrix, target):
        # '074 search a 2d matrix i' is a special case of this problem
        if not matrix or not matrix[0]:
            return False
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False


def main():
    q = Q240()
    m = [[1, 4, 7, 11, 15],
         [2, 5, 8, 12, 19],
         [3, 6, 9, 16, 22],
         [10, 13, 14, 17, 24],
         [18, 21, 23, 26, 30]]
    q.add_args(m, 5)
    q.add_args(m, 20)
    q.run()

if __name__ == '__main__':
    main()
