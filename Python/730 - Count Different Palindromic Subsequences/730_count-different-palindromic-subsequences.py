from leezy import solution, Solution


class Q730(Solution):

    def __init__(self):
        super().__init__()
        self.kMod = 10 ** 9 + 7
        self.memo = []
        self.S = ''
        self.N = 0

    def flat_key_of(self, i, j):
        return self.N * i + j

    def count(self, i, j):
        if i > j:
            return 0
        elif i == j:
            return 1
        key = self.flat_key_of(i, j)
        if self.memo[key] > 0:
            return self.memo[key]

        if self.S[i] == self.S[j]:
            base = self.count(i+1, j-1) * 2
            l, r = i+1, j-1
            while l <= r and self.S[l] != self.S[i]:
                l += 1
            while l <= r and self.S[r] != self.S[i]:
                r -= 1
            if l > r:
                attach = 2
            elif l == r:
                attach = 1
            else:
                attach = - self.count(l+1, r-1)
            ans = base + attach
        else:
            ans = self.count(i+1, j) + self.count(i, j-1) - self.count(i+1, j-1)
        ans = (ans + self.kMod) % self.kMod
        self.memo[key] = ans
        return ans


    @solution
    def countPalindromicSubsequences(self, S):
        self.S = S
        self.N = len(S)
        self.memo = [0] * (len(S) * len(S) + 1)
        ans = self.count(0, self.N - 1)
        return ans


def main():
    q = Q730()
    q.add_case(q.case('bccb'))
    q.add_case(
        q.case('abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'))
    q.run()


if __name__ == '__main__':
    main()
