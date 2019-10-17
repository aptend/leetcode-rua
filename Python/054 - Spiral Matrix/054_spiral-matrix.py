from leeyzer import solution, Solution

class Q054(Solution):
    @solution
    def spiralOrder(self, matrix):
        # 28ms 98.89%
        if len(matrix) == 0:
            return []
        m, n = len(matrix), len(matrix[0])
        total = n
        ans = matrix[0][:]
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        i, j = 0, n-1
        k = 0
        N = m * n
        while total < N:
            for idx, (di, dj) in enumerate(dirs):
                if idx == 0 or idx == 2:
                    k += 1
                if idx % 2 == 0:
                    cnt = m - k
                else:
                    cnt = n - k
                for _ in range(cnt):
                    i, j = i+di, j+dj
                    ans.append(matrix[i][j])
                    total += 1
                if total == N:
                    break
        return ans


def main():
    q = Q054()
    q.add_args([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    q.add_args([[7], [9], [6]])
    q.add_args([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    q.run()

if __name__ == '__main__':
    main()
