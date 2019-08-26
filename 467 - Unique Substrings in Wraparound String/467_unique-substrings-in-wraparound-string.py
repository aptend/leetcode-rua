from leeyzer import Solution, solution


class Q467(Solution):
    @solution
    def findSubstringInWraproundString(self, p):
        # 96ms 72.27%
        res = {i: 1 for i in p}
        l = 1
        for i, j in zip(p, p[1:]):
            # -25 % 26 = 1 because -1 * 26 + 1 = -25
            l = l + 1 if (ord(j) - ord(i)) % 26 == 1 else 1
            res[j] = max(res[j], l)
        return sum(res.values())

    @solution
    def find(self, p):
        # 100ms
        if len(p) == 0:
            return 0
        res = [0] * 26
        BASE = ord('a')
        res[ord(p[0])-BASE] = 1
        l = 1
        for i, j in zip(p, p[1:]):
            # -25 % 26 = 1 because -1 * 26 + 1 = -25
            l = l + 1 if (ord(j) - ord(i)) % 26 == 1 else 1
            res[ord(j)-BASE] = max(res[ord(j)-BASE], l)
        return sum(res)

def main():
    q = Q467()
    q.add_args('a')
    q.add_args('zababc')
    q.run()


if __name__ == "__main__":
    main()
