from leezy import solution, Solution
from collections import defaultdict

class Q149(Solution):

    def slope(self, dx, dy):
        flag = 1 if dx * dy >= 0 else -1
        dx, dy = abs(dx), abs(dy)
        a, b = dx, dy
        while b:
            a, b = b, a % b
        return (flag * (dx // a), dy // a)

    @solution
    def maxPoints(self, points):
        # 84ms 64.97%
        ans = 0
        for x1, y1 in points:
            slopes = defaultdict(int)
            same_point = 0
            for x2, y2 in points:
                dx, dy = x1 - x2, y1 - y2
                if dx == dy == 0:
                    same_point += 1
                elif dy == 0:
                    slopes[(1, 0)] += 1
                else:
                    slopes[self.slope(dx, dy)] += 1
            ans = max(ans, same_point + max(slopes.values(), default=0))
        return ans



def main():
    q = Q149()
    q.add_case(q.case([]).assert_equal(0))
    q.add_case(q.case([[0, 0]]).assert_equal(1))
    q.add_case(q.case([[1, 1], [1, 1], [2, 2], [2, 2]]).assert_equal(4))
    q.add_case(q.case([[1, 1], [2, 2], [3, 3]]).assert_equal(3))
    q.add_case(q.case([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]).assert_equal(4))
    q.run()

if __name__ == '__main__':
    main()
