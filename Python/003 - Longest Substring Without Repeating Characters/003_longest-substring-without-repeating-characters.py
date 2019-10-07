from leeyzer import Solution, solution


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
    q.add_args('abcabcbb')
    q.add_args('bbbbb')
    q.add_args('pwwkew')
    q.add_args('aabbaab!b')
    q.run()


if __name__ == "__main__":
    main()
