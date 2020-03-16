from leezy import solution, Solution


class Q1380(Solution):
    @solution
    def luckyNumbers (self, matrix):
        m = matrix
        min_in_row = [min(enumerate(row), key=lambda p: p[1]) for row in m]
        max_in_col = [max(row[i] for row in m) for i in range(len(m[0]))]
        return [x for c, x in min_in_row if max_in_col[c] == x]


def main():
    q = Q1380()
    q.add_case(q.case([[3, 7, 8], [9, 11, 13], [15, 16, 17]]).assert_equal([15]))
    q.add_case(q.case([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]).assert_equal([12]))
    q.add_case(q.case([[7, 8], [1, 2]]).assert_equal([7]))
    q.add_case(q.case([[8, 8], [8, 8]]).assert_equal([8, 8]))
    q.run()


if __name__ == '__main__':
    main()
