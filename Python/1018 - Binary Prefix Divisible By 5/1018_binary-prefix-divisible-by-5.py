from leezy import solution, Solution


class Q1018(Solution):
    @solution
    def prefixesDivBy5(self, A):
        # 328ms 57.45%
        x = 0
        ans = []
        for i in A:
            x = x * 2 + i
            ans.append(x % 5 == 0)
        return ans


def main():
    q = Q1018()
    q.add_case(q.case([0, 1, 1]).assert_equal([True, False, False]))
    q.run()


if __name__ == '__main__':
    main()
