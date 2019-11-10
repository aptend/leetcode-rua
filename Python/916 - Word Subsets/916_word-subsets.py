from leezy import Solution, solution
from collections import Counter, defaultdict

class Q916(Solution):
    # 1336ms 50.64%
    @solution
    def wordSubsets(self, A, B):
        pattern = defaultdict(int)
        for b in B:
            bcounter = Counter(b)
            for k, v in bcounter.items():
                pattern[k] = max(pattern[k], v)
        ans = []
        for a in A:
            acounter = Counter(a)
            for k, v in pattern.items():
                if acounter[k] < v:
                    break
            else:
                ans.append(a)
        return ans


def main():
    q = Q916()
    q.add_args(['amazon', 'apple', 'facebook', 'google', 'leetcode'], ['e', 'o'])
    q.add_args(['amazon', 'apple', 'facebook', 'google', 'leetcode'], ['e', 'l'])
    q.add_args(['amazon', 'apple', 'facebook', 'google', 'leetcode'], ['e', 'oo'])
    q.add_args(['amazon', 'apple', 'facebook', 'google', 'leetcode'], ['le', 'eo'])
    q.add_args(['amazon', 'apple', 'facebook', 'google', 'leetcode'], ['oc', 'ec', 'ceo'])
    q.run()


if __name__ == "__main__":
    main()
