from leezy import Solution, solution

from collections import Counter

class Q1189(Solution):
    @solution
    def maxNumberOfBalloons(self, text):
        c = Counter(text)
        ans = len(text)
        for ch in 'ban':
            ans = min(ans, c[ch])
        
        for ch in 'lo':
            ans = min(ans, c[ch] // 2)
        return ans


def main():
    q = Q1189()
    q.add_args('nlaebolko')
    q.add_args('leetcode')
    q.add_args('loonbalxballpoon')
    q.run()


if __name__ == "__main__":
    main()
