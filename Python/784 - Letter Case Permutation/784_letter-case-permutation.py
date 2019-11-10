from leezy import Solution, solution


class Q784(Solution):
    @solution
    def letterCasePermutation(self, S):
        total = []
        self.dfs(S, '', total)
        return total

    def dfs(self, s, current, total):
        if not s:
            total.append(current)
            return
        ch = s[0]
        if ch.isdigit():
            self.dfs(s[1:], current+ch, total)
        else:
            self.dfs(s[1:], current+ch.lower(), total)
            self.dfs(s[1:], current+ch.upper(), total)



def main():
    q = Q784()
    q.add_args('a1b2')
    q.run()


if __name__ == "__main__":
    main()
