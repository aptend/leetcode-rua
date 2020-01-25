from leezy import solution, Solution


class Q009(Solution):
    @solution
    def isPalindrome(self, x):
        # 52 ms, 86.17%
        if x < 0:
            return False
        elif x < 10:
            return True
        elif x % 10 == 0:
            return False

        right = 0
        left = x
        while left > right:
            left, r = divmod(left, 10)
            if left == right:
                return True
            right = 10 * right + r
            if left == right:
                return True
        return False


def main():
    q = Q009()
    q.add_case(q.case(121).assert_equal(True))
    q.add_case(q.case(-121).assert_equal(False))
    q.add_case(q.case(10).assert_equal(False))
    q.add_case(q.case(12).assert_equal(False))
    q.add_case(q.case(10001).assert_equal(True))
    q.add_case(q.case(1).assert_equal(True))
    q.add_case(q.case(0).assert_equal(True))
    q.add_case(q.case(21120).assert_equal(False))
    q.run()


if __name__ == '__main__':
    main()
