from leezy import solution, Solution


class Q1012(Solution):
    """
    for 8765:
    XXX             9 * 9 * 8 = 648 
    XX              9 * 9 = 81 
    X               9
    1XXX ~ 7XXX     7 * 9 * 8 * 7 = 3,528  
    80XX ~ 86XX     7 * 8 * 7 = 392  
    870X ~ 875X     6 * 7 = 42 
    8760 ~ 8765     6
    
    648 + 81 + 9 + 3528 + 392 + 42 + 6 = 4706 
    
    8765 - 4706 = 4059
    """
    @solution
    def numDupDigitsAtMostN(self, N):
        # 24ms 100%
        if N <= 10:
            return 0

        def permutation(n, k):
            prod = 1
            for i in range(n-k+1, n+1):
                prod *= i
            return prod

        digits = [int(x) for x in str(N+1)]
        ans = 9
        L = len(digits)
        for i in range(1, L-1):
            ans += 9 * permutation(9, i)
        used = set()
        for i in range(L):
            for j in range(0 if i > 0 else 1, digits[i]):
                if j in used:
                    continue
                if i == L - 1:
                    ans += 1
                else:
                    ans += permutation(9-i, L-i-1)
            if digits[i] in used:
                break
            else:
                used.add(digits[i])
        return N - ans


def main():
    q = Q1012()
    q.add_case(q.case(20).assert_equal(1))
    q.add_case(q.case(100).assert_equal(10))
    q.add_case(q.case(1000).assert_equal(262))
    q.add_case(q.case(8765).assert_equal(4059))
    q.run()


if __name__ == '__main__':
    main()
