from leezy import Solution, solution
from typing import List


class Q253(Solution):
    @solution
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        begins = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        ans = 0
        occupy = 0
        i = j = 0
        while i < len(ends) and j < len(ends):
            if begins[i] < ends[j]:
                occupy += 1
                ans = max(ans, occupy)
                i += 1
            elif begins[i] > ends[j]:
                occupy -= 1
                j += 1
            else:
                i += 1
                j += 1
        return ans


def main():
    q = Q253()
    q.add_args([[0, 30], [5, 10], [15, 20]])
    q.add_args([[7, 10], [2, 4]])
    q.run()


if __name__ == "__main__":
    main()
