from leeyzer import solution, Solution

class Q1252(Solution):
    @solution
    def oddCells(self, n, m, indices):
        # 40ms 100.00%
        rows = [0] * n
        colums = [0] * m
        for i, j in indices:
            rows[i] += 1
            colums[j] += 1
        ans = 0
        for x in rows:
            for y in colums:
                if (x+y) % 2 == 1:
                    ans += 1
        return ans


def main():
    q = Q1252()
    q.add_args(2, 3, [[0, 1], [1, 1]])
    q.run()

if __name__ == '__main__':
    main()
