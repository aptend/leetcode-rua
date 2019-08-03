from leeyzer import Solution, solution


class Q174(Solution):
    @solution
    def calculateMinimumHP(self, dungeon):
        # 48ms 98.29%
        m, n = len(dungeon), len(dungeon[0])
        MAX = float('inf')
        hp = [[MAX]*(n+1) for _ in range(m+1)]
        hp[-1][-2] = 1
        hp[-2][-1] = 1
        # hp[i][j] means minmum hp needed from (i, j) to (m-1, n-1) 
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                hp[i][j] = max(1, min(hp[i+1][j], hp[i][j+1]) - dungeon[i][j])
        return hp[0][0]
    
    @solution
    def minmum_hp(self, dungeon):
        # 168ms 5.12%
        m, n = len(dungeon), len(dungeon[0])
        MIN = float('-inf')
        def can_reach_at_hp(initial_hp):
            # hp[i][j] means maximum hp left from (1, 1) to (i, j)
            hp = [[MIN]*(n+1) for _ in range(m+1)]
            hp[0][1] = hp[1][0] = initial_hp
            for i in range(1, m+1):
                for j in range(1, n+1):
                    hp[i][j] = max(hp[i-1][j], hp[i][j-1]) + dungeon[i-1][j-1]
                    if hp[i][j] < 1:
                        hp[i][j] = MIN # can't saved by magic orbs
            if hp[m][n] > 0:
                return True
            else:
                return False
        lo = 1
        hi = 0
        for j in range(n):
            if dungeon[0][j] < 0:
                hi -= dungeon[0][j]
        for i in range(m):
            if dungeon[i][-1] < 0:
                hi -= dungeon[i][-1]
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if can_reach_at_hp(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo


def main():
    q = Q174()
    q.add_args([[0]])
    q.add_args([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
    q.run()


if __name__ == "__main__":
    main()
