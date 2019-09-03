from leeyzer import Solution, solution


class Q861(Solution):
    @solution
    def matrixScore(self, A):
        # 20ms 93.22%
        # I learned 2 thins from this problem: 
        # 1. when to give up search or simulation 
        # 2. one pattern (binary, dominating part) to think greedy
        m, n = len(A), len(A[0])
        ans = m * (1 << (n-1))
        for j in range(1, n):
            digit_1s = 0
            for i in range(m):
                if A[i][j] == A[i][0]:
                    digit_1s += 1
            ans += max(digit_1s, m-digit_1s) * (1 << (n-1-j))
        return ans


def main():
    q = Q861()
    q.add_args([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]])
    q.run()


if __name__ == "__main__":
    main()
