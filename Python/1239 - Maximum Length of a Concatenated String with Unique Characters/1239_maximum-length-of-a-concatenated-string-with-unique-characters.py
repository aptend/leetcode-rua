from leezy import solution, Solution

class Q1239(Solution):
    @solution
    def maxLength(self, arr):
        # 116ms 25%
        sets = []
        for s in arr:
            st = set(s)
            if len(st) == len(s):
                sets.append(st)
        self.ans = 0
        def dfs(start, cur):
            self.ans = max(self.ans, len(cur))
            for i in range(start, len(sets)):
                if len(cur - sets[i]) == len(cur):
                    cur |= sets[i]
                    dfs(i + 1, cur)
                    cur -= sets[i]
        dfs(0, set())
        return self.ans
        


def main():
    q = Q1239()
    q.add_args(['un', 'iq', 'ue'])
    q.run()

if __name__ == '__main__':
    main()
