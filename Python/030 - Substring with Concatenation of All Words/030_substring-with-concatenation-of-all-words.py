from leezy import solution, Solution
from collections import Counter

class Q030(Solution):
    @solution
    def findSubstring(self, s, words):
        # 712ms 28.94%
        n = len(words[0])
        counter = Counter(words)
        span = sum(len(w) for w in words)
        ans = []
        for i in range(len(s)-span+1):
            if counter == Counter(s[k:k+n] for k in range(i, i+span, n)):
                ans.append(i)
        return ans


def main():
    q = Q030()
    q.add_case(q.case('barfoothefoobarman', ['foo', 'bar']).assert_equal([0, 9]))
    q.run()

if __name__ == '__main__':
    main()
