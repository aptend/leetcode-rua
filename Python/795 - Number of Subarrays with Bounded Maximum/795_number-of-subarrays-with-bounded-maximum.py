from leezy import Solution, solution


class Q795(Solution):
    @solution
    def numSubarrayBoundedMax(self, A, L, R):
        # 372ms 100.00%
        # dp[i] means max length of valid subarry ending with A[i]
        dp = 0
        ans = 0
        # previous position of A[prev], which is greater than R
        prev = -1
        for i in range(len(A)):
            if A[i] < L:
                # dp[i] = dp[i-1] -> dp = dp 
                ans += dp
            elif A[i] > R:
                dp = 0
                prev = i
            else:
                # [prev+1, i] contains elements who are less than R
                dp = i - prev
                ans += dp
        return ans

    @solution
    def num_subarray_bounded_max(self, A, L, R):
        def at_most(k):
            ans = accum = 0
            for x in A:
                if x > k:
                    accum = 0
                else:
                    accum += 1
                ans += accum
            return ans

        return at_most(R) - at_most(L-1)


def main():
    q = Q795()
    q.add_case(q.case([1, 1, 2, 4, 3], 2, 3).assert_equal(4))
    q.run()


if __name__ == "__main__":
    main()
