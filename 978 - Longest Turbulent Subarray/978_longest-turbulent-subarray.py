from leeyzer import Solution, solution


class Q978(Solution):
    @solution
    def maxTurbulenceSize(self, A):
        N = len(A)
        if N == 1:
            return 1
        dp = [1, 1 if A[0] == A[1] else 2] + [0] * (N-2)
        for i, n in enumerate(A[2:], 2):
            if n == A[i-1]:
                dp[i] = 1
            elif n < A[i-1] and A[i-1] > A[i-2]:
                dp[i] = dp[i-1] + 1
            elif n > A[i-1] and A[i-1] < A[i-2]:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 2
        return max(dp)

    @solution
    def tubulence(self, A):
        N = len(A)
        if N == 1:
            return 1
        dp = 1 if A[0] == A[1] else 2
        g_max = dp
        for i, n in enumerate(A[2:], 2):
            if n == A[i-1]:
                dp = 1
            elif n < A[i-1] and A[i-1] > A[i-2]:
                dp += 1
            elif n > A[i-1] and A[i-1] < A[i-2]:
                dp += 1
            else:
                dp = 2
            g_max = max(g_max, dp)
        return g_max

    @solution
    def turb(self, A):
        g_max = up = down = 1
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                down = up + 1
                up = 1
            elif A[i] > A[i-1]:
                up = down + 1
                down = 1
            else:
                up = down = 1
            g_max = max(g_max, up, down)
        return g_max

        




def main():
    q = Q978()
    q.add_args([9, 4, 2, 10, 7, 8, 8, 1, 9]) # 5
    q.add_args([4, 8, 12, 16]) # 2
    q.add_args([100]) # 1
    q.add_args([10, 10]) # 1
    q.run()


if __name__ == "__main__":
    main()
