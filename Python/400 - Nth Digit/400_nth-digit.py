from leezy import solution, Solution


class Q400(Solution):
    @solution
    def findNthDigit(self, n):
        # 28ms 63.10%
        unit = 1
        unit_cnt = 9
        while n > unit * unit_cnt:
            n -= unit * unit_cnt
            unit += 1
            unit_cnt *= 10
        i, j = divmod(n-1, unit)
        num = 10 ** (unit-1) + i
        return int(str(num)[j])


def main():
    q = Q400()
    q.add_case(q.case(3))
    q.add_case(q.case(11))
    q.run()

if __name__ == '__main__':
    main()
