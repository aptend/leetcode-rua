from leezy import solution, Solution


class Q1004(Solution):
    @solution
    def longestOnes(self, A, K):
        # 684ms 68.83%
        z_count = 0
        i = 0
        N = len(A)
        ans = 0
        for j in range(N):
            if A[j] == 0:
                z_count += 1
            while z_count > K:
                if A[i] == 0:
                    z_count -= 1
                i += 1
            ans = max(ans, j - i + 1)
        return ans


def main():
    q = Q1004()
    q.add_case(q.case([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
    q.run()

if __name__ == '__main__':
    main()
