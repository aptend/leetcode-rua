from leeyzer import Solution, solution


class Q739(Solution):
    @solution
    def dailyTemperatures(self, T):
        # 428ms 88.54%
        # I think the time complexity is O(n)
        # every temperature will be visited at most twice
        ans = [0] * len(T)
        mono_stack = [0]
        for idx, t in enumerate(T[1:], 1):
            while mono_stack and t > T[mono_stack[-1]]:
                pidx = mono_stack.pop()
                ans[pidx] = idx - pidx
            mono_stack.append(idx)
        return ans


def main():
    q = Q739()
    q.add_args([42])
    q.add_args([73, 74, 75, 71, 69, 72, 76, 73])
    q.run()


if __name__ == "__main__":
    main()
