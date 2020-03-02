from leezy import solution, Solution
from bisect import bisect_right


class Q768(Solution):
    @solution
    def maxChunksToSorted(self, arr):
        # 76 ms, 82.71%
        stack = [arr[0]]
        for x in arr[1:]:
            if x >= stack[-1]:
                stack.append(x)
            else:
                idx = bisect_right(stack, x)
                stack[idx:] = [stack[-1]]
        return len(stack)


def main():
    q = Q768()
    q.add_case(q.case([5, 4, 3, 2, 1]).assert_equal(1))
    q.add_case(q.case([5, 4, 3, 2, 1, 4]).assert_equal(1))
    q.add_case(q.case([5, 4, 3, 2, 1, 7]).assert_equal(2))
    q.add_case(q.case([2, 1, 3, 4, 4]).assert_equal(4))
    q.run()


if __name__ == '__main__':
    main()
