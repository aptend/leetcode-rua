from leezy import solution, Solution

class Q1262(Solution):
    @solution
    def maxSumDivThree(self, nums):
        # 316ms
        dp0 = 0
        dp1 = float('-inf')
        dp2 = float('-inf')
        for x in nums:
            r = x % 3
            if r == 0:
                dp0 += x
                dp1 += x
                dp2 += x
            else:
                d0, d1, d2 = dp0, dp1, dp2
                if r == 1:
                    dp0 = max(d0, d2+x)
                    dp1 = max(d1, d0+x)
                    dp2 = max(d2, d1+x)
                else:
                    dp0 = max(d0, d1+x)
                    dp1 = max(d1, d2+x)
                    dp2 = max(d2, d0+x)
        return dp0


def main():
    q = Q1262()
    q.add_case(q.case([3, 6, 5, 1, 8]).assert_equal(18))
    q.add_case(q.case([4]).assert_equal(0))
    q.add_case(q.case([1, 2, 3, 4, 4]).assert_equal(12))
    q.run()

if __name__ == '__main__':
    main()
