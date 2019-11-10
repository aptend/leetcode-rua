from leezy import solution, Solution

from collections import Counter

class Q1234(Solution):
    @solution
    def balancedString(self, s):
        # briliant
        c = Counter(s)
        N = len(s)
        i = 0
        win = N
        for j, ch in enumerate(s):
            # move ch into [i, j] subarray
            c[ch] -= 1
            while i < N and all(c[u] <= N // 4 for u in 'QWER'):
                win = min(win, j - i + 1)
                # move s[i] out of [i, j] subarray
                c[s[i]] += 1
                i += 1
        return win



def main():
    q = Q1234()
    q.add_args('QWER')
    q.add_args('QQQQ')
    q.run()

if __name__ == '__main__':
    main()
