from leezy import solution, Solution


class Q1386(Solution):
    @solution
    def maxNumberOfFamilies(self, n, reservedSeats):

        def calc_row(row):
            left = mid = right = True
            for x in row:
                if 2 <= x <= 5:
                    left = False
                if 4 <= x <= 7:
                    mid = False
                if 6 <= x <= 9:
                    right = False
            if left and mid and right:
                return 2
            elif left or mid or right:
                return 1
            else:
                return 0

        reserved = sorted(reservedSeats)
        i, j = reserved[0]
        row = [j]
        ridx = i
        ans = 0
        for i, j in reserved[1:]:
            if ridx != i:
                ans += calc_row(row)
                ridx = i
                n -= 1
                row.clear()
            row.append(j)
        ans += calc_row(row)
        n -= 1
        return ans + n * 2


def main():
    q = Q1386()
    q.add_case(q.case(3, [[1, 2], [1, 3], [1, 8], [
               2, 6], [3, 1], [3, 10]]).assert_equal(4))
    q.add_case(q.case(2, [[2, 1], [1, 8], [2, 6]]).assert_equal(2))
    q.add_case(q.case(4, [[4, 3], [1, 4], [4, 6], [1, 7]]).assert_equal(4))
    q.run()


if __name__ == '__main__':
    main()
