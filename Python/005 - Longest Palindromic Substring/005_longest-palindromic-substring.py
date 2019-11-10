from leezy import Solution, solution


class RabinKarp:
    def __init__(self, text, M, R=128, Q=100000037):
        self.R = R
        self.M = M
        self.Q = Q
        self.text = text
        self.text_inv = text[::-1]
        pow = 1
        for _ in range(1, M):
            pow = (R * pow) % Q
        self.pow = pow  # R^(M-1) % Q

        self.invR, _ = self._exgcd(R, Q)
        if self.invR < 0:
            self.invR = self.invR % Q + Q

    def dummy_hash(self, s):
        h = 0
        for c in s:
            h = (h * self.R + ord(c)) % self.Q
        return h

    def _exgcd(self, a, b):
        """omit remainder here
        """
        if b == 0:
            return 1, 0  # 1 = 1*1 + 0*0
        x, y = self._exgcd(b, a % b)
        return y, x - (a//b)*y

    def gen_hash(self):
        txt, pow, R, M, Q = self.text, self.pow, self.R, self.M, self.Q
        txt_hash = self.dummy_hash(txt[:M])
        yield txt_hash
        for i in range(M, len(txt)):
            txt_hash = (txt_hash + Q - pow * ord(txt[i-M]) % Q) % Q
            txt_hash = (txt_hash * R + ord(txt[i])) % Q
            yield txt_hash

    def gen_hash_inv(self):
        txt, pow, invR, M, Q = self.text_inv, self.pow, self.invR, self.M, self.Q
        txt_hash = self.dummy_hash(txt[-M:])
        yield txt_hash
        for i in range(len(txt)-M-1, -1, -1):
            txt_hash -= ord(txt[i+M])
            txt_hash = (txt_hash * invR) % Q
            txt_hash += ord(txt[i])*pow
            txt_hash = txt_hash % Q
            yield txt_hash


def can_solve_at(s, L):
    rk = RabinKarp(s, L)
    i = 0
    for h, h_inv in zip(rk.gen_hash(), rk.gen_hash()):
        if h == h_inv and s[i:i+L] == ''.join(reversed(s[i:i+L])):
            return i
        i += 1
    return -1


class Q005(Solution):
    @solution
    def longestPalindrome(self, s):
        t = "#"+s
        dp = [0]
        res, g_max = "", 0
        for i in range(1, len(t)):
            new_dp = []
            for skip in dp:
                if t[i - 1 - skip] == t[i]:
                    new_dp.append(skip + 2)
            new_dp.append(1)
            new_dp.append(0)
            dp = new_dp
            cur_max = max(dp)
            if cur_max > g_max:
                g_max = cur_max
                res = t[i-g_max+1:i+1]
        return res

    @solution
    def longest(self, s):
        def expand(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return i+1, j
        res, g_max = "", 0
        for c in range(len(s)):
            i, j = expand(c, c)
            if j-i > g_max:
                g_max = j-i
                res = s[i:j]
            i, j = expand(c, c+1)
            if j-i > g_max:
                g_max = j-i
                res = s[i:j]
        return res

    @solution
    def longest_RK(self, s):
        if not s:
            return ''
        res = s[0]
        lo, hi = 1, len(s) // 2
        while lo <= hi:
            mid = (lo + hi) // 2
            idx_even = can_solve_at(s, 2*mid)
            idx_odd = can_solve_at(s, 2*mid+1)
            if idx_odd >= 0:
                idx, L = idx_odd, 2*mid+1
            else:
                idx, L = idx_even, 2*mid
            if idx >= 0:
                if L > len(res):
                    res = s[idx:idx+L]
                lo = mid + 1
            else:
                hi = mid - 1
        return res


def main():
    q = Q005()
    q.add_args('')
    q.add_args('a')
    q.add_args('abadd')
    q.add_args('aaaaa')
    q.add_args('babadaba')
    q.run()


if __name__ == "__main__":
    main()
