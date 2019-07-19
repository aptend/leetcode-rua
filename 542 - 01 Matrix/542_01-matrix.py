from leeyzer import Solution, solution


class Q542(Solution):
    @solution
    def updateMatrix(self, matrix):
        MAX = float('inf')
        m, n = len(matrix), len(matrix[0])
        ans = [[MAX]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    if i > 0:
                        ans[i][j] = min(ans[i][j], ans[i-1][j]+1)
                    if j > 0:
                        ans[i][j] = min(ans[i][j], ans[i][j-1]+1)
                else:
                    ans[i][j] = 0
                if i > 0:
                    ans[i][j]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j]:
                    if i < m-1:
                        ans[i][j] = min(ans[i][j], ans[i+1][j]+1)
                    if j < n-1:
                        ans[i][j] = min(ans[i][j], ans[i][j+1]+1)
        return ans

    
def main():
    q = Q542()
    q.add_args([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    q.add_args(
        [[0, 0, 0],
         [0, 1, 0],
         [1, 1, 1]]
    )
    q.run()


if __name__ == "__main__":
    main()
