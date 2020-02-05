from leezy import solution, Solution
from math import sqrt

class Q829(Solution):
    @solution
    def consecutiveNumbersSum(self, N):
        # TLE
        table = set()
        prev = 0
        ans = 0 if N == 1 else 1
        for i in range((N+1)//2+1):
            prev += i
            if prev - N in table:
                ans += 1
            table.add(prev)
        return ans
    
    @solution
    def consecutive_number_sum(self, N):
        # N = (x+1) + (x+2) + ... + (x+k)
        # N = kx + (1 + 2 + ... + k) = kx + (1 + k) * k / 2
        k = s = 1
        ans = 0
        while s <= N:
            if (N - s) % k == 0:
                ans += 1
            k += 1
            s = (k + 1) * k / 2
        return ans

def main():
    q = Q829()
    q.add_case(q.case(5).assert_equal(2))
    q.add_case(q.case(1).assert_equal(1))
    q.add_case(q.case(6).assert_equal(2))
    q.add_case(q.case(4).assert_equal(1))
    q.add_case(q.case(15).assert_equal(4))
    q.add_case(q.case(9).assert_equal(3))
    q.run()


if __name__ == '__main__':
    main()
