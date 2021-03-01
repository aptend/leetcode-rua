from leezy import solution, Solution


class Q1124(Solution):
    @solution
    def longestWPI(self, hours):
        # 240 ms, 50.87%
        deltas = [1 if h > 8 else -1 for h in hours]
        accum = 0
        memo = {}
        ans = 0
        for i in range(len(deltas)):
            accum += deltas[i]
            if accum > 0:
                ans = i + 1
            if accum - 1 in memo:
                ans = max(ans, i - memo[accum - 1])
            if accum not in memo:
                memo[accum] = i
        return ans


def main():
    q = Q1124()
    q.add_case(q.case([9, 9, 6, 0, 6, 6, 9]))
    q.run()


if __name__ == '__main__':
    main()
