from leezy import solution, Solution
from itertools import chain
from bisect import bisect_left

class Q354(Solution):
    @solution
    def maxEnvelopes(self, envelopes):
        # TLE
        N = len(envelopes)
        if N <= 1:
            return N
        envs = sorted(envelopes)
        groups = []
        group = [envs[0][1]]
        prev = envs[0][0]
        for x, y in envs[1:]:
            if x != prev:
                groups.append(group[:])
                group.clear()
                prev = x
            group.append(y)
        groups.append(group)
        dp = [0] * N
        idx = 0
        for i, group in enumerate(groups):
            for x in group:
                max_l = 0
                for j, y in enumerate(chain.from_iterable(groups[:i])):
                    if x > y:
                        max_l = max(max_l, dp[j])
                dp[idx] = max_l+1
                idx += 1
        return max(dp)

    @solution
    def max_env(self, envs):
        # 152 ms faster than 91.94%
        hay = [p[1] for p in sorted(envs, key=lambda e: (e[0], -e[1]))]
        stack = []
        for x in hay:
            idx = bisect_left(stack, x)
            if idx >= len(stack):
                stack.append(x)
            else:
                stack[idx] = x
        return len(stack)



def main():
    q = Q354()
    q.add_case(q.case([[5, 4], [6, 2]]))
    q.add_case(q.case([[5, 4], [6, 4], [6, 7], [2, 3]]))
    q.add_case(q.case([[5, 4], [6, 4], [6, 7], [2, 3], [7, 4], [7, 7], [7, 8]]))
    q.run()


if __name__ == '__main__':
    main()
