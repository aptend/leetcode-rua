from leezy import solution, Solution

class Q048(Solution):
    @solution
    def rotate(self, matrix):
        # 36ms 96.45%
        N = len(matrix)
        for i in range(N):
            for j in range(i+1,N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
        return matrix

    @solution
    def rot(self, matrix):
        # matrix[i][j] → matrix[j][n−i−1] → matrix[n−i−1][n−j−1] → matrix[n−j−1][i]
        N = len(matrix)
        for i in range(N // 2):
            for j in range(i, N-i-1):
                matrix[i][j], matrix[j][N-1-i], matrix[N-1-i][N-j-1], matrix[N-1-j][i] = \
                    matrix[N-1-j][i] ,matrix[i][j], matrix[j][N-1-i], matrix[N-1-i][N-j-1]
        return matrix



def main():
    q = Q048()
    q.add_args([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    q.run()

if __name__ == '__main__':
    main()
