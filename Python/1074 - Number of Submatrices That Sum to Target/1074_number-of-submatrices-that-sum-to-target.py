from leezy import solution, Solution
from collections import defaultdict

class Q1074(Solution):
    @solution
    def numSubmatrixSumTarget(self, matrix, target):
        # 6456ms 73.51%
        n = len(matrix[0])
        acc_m = []
        for row in matrix:
            acc_row = [0]
            for x in row:
                acc_row.append(acc_row[-1] + x)
            acc_m.append(acc_row)

        ans = 0
        for i in range(1, n+1):
            for j in range(i, n+1):
                c = defaultdict(int)
                c[0] = 1
                acc = 0
                for row in acc_m:
                    acc += row[j] - row[i-1]
                    ans += c[acc - target]
                    c[acc] += 1
        return ans


def main():
    q = Q1074()
    q.add_case(q.case([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0).assert_equal(4))
    q.add_case(q.case([[1, -1], [-1, 1]], 0).assert_equal(5))
    q.run()

if __name__ == '__main__':
    main()
