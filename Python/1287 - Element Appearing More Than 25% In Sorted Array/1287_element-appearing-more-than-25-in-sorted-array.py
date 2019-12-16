from collections import Counter
from leezy import solution, Solution
from typing import List


class Q1287(Solution):
    @solution
    def findSpecialInteger(self, arr: List[int]) -> int:
        return Counter(arr).most_common()[0][0]


def main():
    q = Q1287()
    q.add_case(q.case([1, 2, 2, 6, 6, 6, 6, 7, 10]))
    q.run()

if __name__ == '__main__':
    main()
