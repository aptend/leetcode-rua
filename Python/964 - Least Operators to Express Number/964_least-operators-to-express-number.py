from leezy import solution, Solution

from heapq import heappush, heappop
from math import log, floor


class Q964(Solution):
    @solution
    def leastOpsExpressTarget(self, x, target):
        seen = set()
        heap = [(0, target)]
        while heap:
            print(heap)
            cost, val = heappop(heap)
            if val == 0:
                return cost - 1
            pow_n = floor(log(val, x))
            # we allow two arms to push the same value_next once
            if val in seen:
                continue
            seen.add(val)
            val_next = val - x ** pow_n
            new_cost = cost + (2 if pow_n == 0 else pow_n)
            heappush(heap, (new_cost, val_next))

            val_next = x ** (pow_n + 1) - val
            new_cost = cost + pow_n + 1
            heappush(heap, (new_cost, val_next))



def main():
    q = Q964()
    q.add_case(q.case(3, 19).assert_equal(5))
    q.add_case(q.case(5, 501).assert_equal(8))
    q.add_case(q.case(100, 100000000).assert_equal(3))
    q.add_case(q.case(3, 365).assert_equal(17))
    q.run()


if __name__ == '__main__':
    main()
