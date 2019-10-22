from leeyzer import solution, Solution

from collections import Counter
class Q076(Solution):
    @solution
    def minWindow(self, s, t):
        # 140ms 55.07%
        # link to 424 1234
        count = Counter(t)
        i, N = 0, len(count)
        ans = ''
        L = float('inf')
        formed = 0
        for j, ch in enumerate(s):
            if ch in count:
                count[ch] -= 1
                if count[ch] == 0:
                    formed += 1
            while formed == N:
                if j + 1 - i < L:
                    ans = s[i: j + 1]
                    L = j + 1 - i
                if s[i] in count:
                    count[s[i]] += 1
                    if count[s[i]] > 0:
                        formed -= 1
                i += 1
        return ans


def main():
    q = Q076()
    q.add_args('ADOBECODEBANC', 'ABC')
    q.run()

if __name__ == '__main__':
    main()
