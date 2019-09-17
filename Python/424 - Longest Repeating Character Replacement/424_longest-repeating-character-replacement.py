from leeyzer import Solution, solution

from collections import defaultdict

class Q424(Solution):
    @solution
    def characterReplacement(self, s, k):
        # 108ms 92.61%
        counter = defaultdict(int)
        max_freq = 0
        i, j = 0, 0
        ans = 0
        while j < len(s):
            counter[s[j]] += 1
            max_freq = max(max_freq, counter[s[j]])
            if j - i + 1 - max_freq > k:
                ans = max(ans, j - i)
                counter[s[i]] -= 1
                i += 1
            j += 1
        ans = max(ans, j - i)
        return ans


def main():
    q = Q424()
    q.add_args('ABAB', 2)
    q.add_args('ABAA', 0)
    q.add_args('ABAB', 1)
    q.add_args('AABABBA', 1)
    q.run()


if __name__ == "__main__":
    main()
