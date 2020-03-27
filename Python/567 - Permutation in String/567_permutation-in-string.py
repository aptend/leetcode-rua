from leezy import solution, Solution
from collections import Counter

class Q567(Solution):
    @solution
    def checkInclusion(self, s1, s2):
        # 76 ms 54.67%
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        c = Counter(s1)
        nonzero = len(c)
        for i, ch in enumerate(s2):
            if ch in c:
                if c[ch] == 0:
                    nonzero += 1
                c[ch] -= 1
                if c[ch] == 0:
                    nonzero -= 1
                    if nonzero == 0:
                        return True
            if i >= n1-1:
                ch = s2[i - n1 + 1]
                if ch in c:
                    if c[ch] == 0:
                        nonzero += 1
                    c[ch] += 1
                    if c[ch] == 0:
                        nonzero -= 1
        return False


def main():
    q = Q567()
    q.add_case(q.case('ab', 'eidbaooo'))
    q.add_case(q.case('ab', 'eidboaoo'))
    q.add_case(q.case('ab', 'bba'))
    q.run()


if __name__ == '__main__':
    main()
