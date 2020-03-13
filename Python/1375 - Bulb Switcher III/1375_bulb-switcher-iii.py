from leezy import solution, Solution


class Q1375(Solution):
    @solution
    def numTimesAllBlue(self, light):
        max_num_blub = -1
        ans = 0
        for (i, x) in enumerate(light, 1):
            max_num_blub = max(max_num_blub, x)
            if max_num_blub == i:
                ans += 1
        return ans


def main():
    q = Q1375()
    q.add_case(q.case([2, 1, 3, 5, 4]).assert_equal(3))
    q.add_case(q.case([3, 2, 4, 1, 5]).assert_equal(2))
    q.add_case(q.case([4, 1, 2, 3]).assert_equal(1))
    q.add_case(q.case([2, 1, 4, 3, 6, 5]).assert_equal(3))
    q.add_case(q.case([1, 2, 3, 4, 5, 6]).assert_equal(6))
    q.run()


if __name__ == '__main__':
    main()
