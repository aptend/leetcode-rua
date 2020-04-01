from leezy import solution, Solution


class Q1111(Solution):
    @solution
    def maxDepthAfterSplit(self, seq):
        # 48ms
        max_nest = 0
        left = 0
        for ch in seq:
            if ch == '(':
                left += 1
                max_nest = max(left, max_nest)
            else:
                left -= 1
        n = max_nest // 2

        ans = [0] * len(seq)
        stack = []
        B_cnt = 0
        for i, ch in enumerate(seq):
            if ch == '(':
                if len(stack) < n:
                    stack.append(i)
                else:
                    B_cnt += 1
                    ans[i] = 1
            else:
                if B_cnt > 0:
                    B_cnt -= 1
                    ans[i] = 1
                else:
                    stack.pop()
        return ans


def main():
    q = Q1111()
    q.add_case(q.case('(()())'))
    q.add_case(q.case('()(())()'))
    q.run()


if __name__ == '__main__':
    main()
