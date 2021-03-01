from leezy import solution, Solution

from collections import Counter

class Q395(Solution):
    @solution
    def longestSubstring(self, s, k):
        #   time used & rank: 48 ms faster than 43.16%
        # memory used & rank: 15 MB less than 61.36%
        if not s:
            return 0
        split_set = set(ch for ch, cnt in Counter(s).items() if cnt < k)
        if len(split_set) == 0:
            return len(s)
        i = 0
        ans = 0
        for j in range(len(s)):
            if s[j] in split_set:
                ans = max(ans, self.longestSubstring(s[i:j], k))
                i = j + 1
        ans = max(ans, self.longestSubstring(s[i:], k))
        return ans


def main():
    q = Q395()
    q.add_case(q.case('aaabb', 3).assert_equal(3))
    q.add_case(q.case("bbaaacbd", 3).assert_equal(3))
    q.run()


if __name__ == '__main__':
    main()
