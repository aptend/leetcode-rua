from leezy import Solution, solution


class Q801(Solution):
    @solution
    def minSwap(self, A, B):
        # 72ms 66.80%
        # dp0 means minimum swaps needed to sort A and B w/o swapping the last column
        # dp1 means minimum swaps needed to sort A and B w/ swapping the last column
        dp0 = dp1 = 1
        MAX = float('inf')
        for i in range(1, len(A)):
            # s00: don't swap current column when previous column was not swapped
            # s10: swap current column when previous column was not swapped
            # s01: ..
            # s11: ..
            s00 = s01 = s10 = s11 = MAX
            if A[i] > A[i-1] and B[i] > B[i-1]:
                s00 = dp0
                s11 = dp1 + 1
            if A[i] > B[i-1] and B[i] > A[i-1]:
                s01 = dp1
                s10 = dp0 + 1
            dp0, dp1 = min(s00, s01), min(s10, s11)
        return min(dp0, dp1)

def main():
    q = Q801()
    q.add_args([1, 3, 5, 4], [1, 2, 3, 7])
    q.add_args([1, 2, 5, 4], [1, 3, 3, 7])
    q.run()


if __name__ == "__main__":
    main()
