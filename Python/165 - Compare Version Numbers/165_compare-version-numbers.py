from leezy import solution, Solution
from itertools import zip_longest

class Q165(Solution):
    @solution
    def compareVersion(self, version1, version2):
        p1 = [int(x) for x in version1.split('.')]
        p2 = [int(x) for x in version2.split('.')]
        n1, n2 = len(p1), len(p2)
        if n1 < n2:
            p1.extend([0] * (n2-n1))
        else:
            p2.extend([0] * (n1-n2))
        if p1 < p2:
            return -1
        elif p1 > p2:
            return 1
        else:
            return 0

    @solution
    def compare(self, v1, v2):
        p1 = [int(x) for x in v1.split('.')]
        p2 = [int(x) for x in v2.split('.')]
        for x, y in zip_longest(p1, p2, fillvalue=0):
            if x > y:
                return 1
            elif x < y:
                return -1
        return 0


def main():
    q = Q165()
    q.add_case(q.case('0.1', '1.1').assert_equal(-1))
    q.add_case(q.case('1.0.1', '1').assert_equal(1))
    q.add_case(q.case('7.5.2.4', '7.5.3').assert_equal(-1))
    q.add_case(q.case('1.01', '1.001').assert_equal(0))
    q.add_case(q.case('1', '1.0.0').assert_equal(0))
    q.run()


if __name__ == '__main__':
    main()
