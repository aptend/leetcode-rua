from leezy import solution, Solution
from heapq import heapify, heapreplace

class Q1354(Solution):
    @solution
    def isPossible(self, target):
        heap = [-t for t in target]
        heapify(heap)
        ones = target.count(1)
        s = sum(target)
        N = len(target)
        while ones < N:
            pivot = -heap[0]
            left_sum = s - pivot
            if left_sum == 1:
                return True
            if left_sum == 0 or left_sum >= pivot:
                return False
            x = pivot % left_sum
            if x == 0:
                return False
            if x == 1:
                ones += 1
            s -= pivot - x
            heapreplace(heap, -x)
        return True


def main():
    q = Q1354()
    q.add_case(q.case([1, 1, 999999999]).assert_equal(True))
    q.add_case(q.case([9, 3, 5]).assert_equal(True))
    q.add_case(q.case([1, 10000000]).assert_equal(True))
    q.add_case(q.case([2, 90000002]).assert_equal(False))
    q.run()


if __name__ == '__main__':
    main()
