from leeyzer import Solution, solution


class Q875(Solution):
    @solution
    def minEatingSpeed(self, piles, H):
        # 384ms 70.59%
        lo = max(sum(p // H for p in piles), 1)
        hi = max(piles)
        while lo <= hi:
            m = lo + (hi - lo) // 2
            cost = sum((p + m - 1) // m for p in piles)
            if cost <= H:
                hi = m - 1
            else:
                lo = m + 1
        return lo



def main():
    q = Q875()
    q.add_args([3, 6, 7, 11], 8)
    q.add_args([30, 11, 23, 4, 20], 5)
    q.add_args([30, 11, 23, 4, 20], 6)
    q.add_args([30, 11, 23, 4, 20], 100)
    q.run()


if __name__ == "__main__":
    main()
