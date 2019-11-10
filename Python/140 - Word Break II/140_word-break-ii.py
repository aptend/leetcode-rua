from leezy import Solution, solution


class Q140(Solution):
    @solution
    def wordBreak(self, s, wordDict):
        # 32ms 80.33%
        word_dict = set(wordDict)
        memo = {len(s): []}
        def sub_problem(i):
            if i in memo:
                return memo[i]
            solns = []
            if s[i:] in word_dict:
                solns.append(s[i:])
            for j in range(i, len(s)):
                word = s[i:j+1]
                if word in word_dict:
                    solns.extend(
                        word + ' ' + item for item in sub_problem(j+1))
            memo[i] = solns
            return solns
        return sub_problem(0)


def main():
    q = Q140()
    q.add_args('aaaaaaa', ['a', 'aa', 'aaaa'])
    q.add_args('catsanddog', ['cat', 'cats', 'and', 'sand', 'dog'])
    q.add_args('catsandog', ['cat', 'cats', 'and', 'sand', 'dog'])
    q.add_args('pineapplepenapple', ["apple", "pen", "applepen", "pine", "pineapple"])
    q.run()


if __name__ == "__main__":
    main()
