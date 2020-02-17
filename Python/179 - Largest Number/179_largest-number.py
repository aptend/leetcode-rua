from leezy import solution, Solution
from functools import cmp_to_key


class Wrap:
    def __init__(self, x):
        self.x = str(x)

    def __eq__(self, other):
        return self.x == self.x

    def __lt__(self, other):
        return self.x + other.x < other.x + self.x


class Q179(Solution):
    @solution
    def largestNumber(self, nums):
        def cmp(s, t):
            # s=3 t=34
            # 334 < 343, so we get a smaller val by arraging s first
            # which means s is smaller than t
            if s + t < t + s:
                return -1
            else:
                return 1

        literal_nums = [str(n) for n in nums]
        r = "".join(sorted(literal_nums, key=cmp_to_key(cmp), reverse=True))
        return "0" if r[0] == "0" else r

    @solution
    def largest(self, nums):
        l_nums = [str(n) for n in nums]
        r = "".join(sorted(l_nums, key=lambda x: Wrap(x), reverse=True))
        return "0" if r[0] == "0" else r


def main():
    q = Q179()
    q.add_case(q.case([10, 2]).assert_equal("210"))
    q.add_case(q.case([3, 30, 34, 5, 9]).assert_equal("9534330"))
    q.run()


if __name__ == '__main__':
    main()
