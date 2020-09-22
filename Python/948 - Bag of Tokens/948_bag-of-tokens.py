from leezy import solution, Solution


class Q948(Solution):
    @solution
    def bagOfTokensScore(self, tokens, P):
        # 72 ms faster than 58.99%
        tokens = sorted(tokens)
        if not tokens or P < tokens[0]:
            return 0

        i, j = 0, len(tokens)-1
        ans = 0
        while i <= j:
            while i <= j and tokens[i] <= P:
                P -= tokens[i]
                i += 1
                ans += 1
            if i == j: # the last one token, do not face down
                break
            if i < j:
                P += tokens[j]
                j -= 1
                ans -= 1
        return ans


def main():
    q = Q948()
    q.add_case(q.case([100, 200, 300], 50).assert_equal(0))
    q.add_case(q.case([100, 200], 150).assert_equal(1))
    q.add_case(q.case([100, 200, 300, 400], 200).assert_equal(2))
    q.run()


if __name__ == '__main__':
    main()
