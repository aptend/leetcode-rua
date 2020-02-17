from leezy import Solution, solution


class Q003(Solution):
    @solution
    def lengthOfLongestSubstring(self, s):
        j = 0
        ans = 0
        seen = {}
        for i, ch in enumerate(s):
            if ch in seen:
                j = max(j, seen[ch] + 1)
            seen[ch] = i
            ans = max(ans, i - j + 1)
        return ans

    @solution
    def length(self, s):
        j = 0
        ans = 0
        seen = {}
        for i, ch in enumerate(s):
            if ch in seen:
                ans = max(ans, i - j)
                j = max(j, seen[ch] + 1)
            seen[ch] = i
        ans = max(ans, len(s) - j)
        return ans


def main():
    q = Q003()
    q.add_case(q.case('abcabcbb').assert_equal(3))
    q.add_case(q.case('bbbbb').assert_equal(1))
    q.add_case(q.case('pwwkew').assert_equal(3))
    q.add_case(q.case('aabbaab!b').assert_equal(3))
    q.add_case(q.case('abcd').assert_equal(4))
    q.run()


if __name__ == "__main__":
    main()
