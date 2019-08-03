from leeyzer import Solution, solution

from bisect import bisect_right

class Q378(Solution):
    @solution
    def kthSmallest(self, matrix, k):
        # 140ms 98.05%
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo <= hi:
            m = lo + (hi - lo) // 2
            le = 0
            for row in matrix:
                le += bisect_right(row, m)
            if le >= k:
                hi = m - 1
            else:
                lo = m + 1
        return lo
    
    @solution
    def kth_smallest_better(self, matrix, k):
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo <= hi:
            m = lo + (hi - lo) // 2
            le = 0
            for row in matrix:
                le += bisect_right(row, m)
                if le == 0 or le >= k:
                    break
            if le >= k:
                hi = m - 1
            else:
                lo = m + 1
        return lo


def main():
    q = Q378()
    q.add_args([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)
    q.run()


if __name__ == "__main__":
    main()
