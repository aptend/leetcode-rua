from leeyzer import Solution, solution


class Q04(Solution):
    @solution
    def domino_dp_greedy(self, n, m, broken):
        # https://www.bilibili.com/video/av68891116/?p=3
        # TLE 11/94
        # n * 2^m * 2 ^m * n
        # 8 * 256 * 256 * 8 * C ?
        brk = set(tuple(b) for b in broken)
        N = 1 << m
        # dp[i] means maximum of dominos on the board
        # when last row was occupied as integer 'i' claimed
        # e.g. i = 7 = b0111 means row[0]、row[1] and row[2] are occupied
        dp = [-1] * N
        dp[N-1] = 0

        def nth_bit(x, n):
            return (x >> n) & 1

        for i in range(n): # iter over n rows
            next_dp = [-1] * N
            for s in range(N): # for every state of last row
                if dp[s] == -1: # invalid state
                    continue

                for cur in range(N):
                    # first we need to check if we can turn `s` into `cur`
                    invalid_cur = False
                    for j in range(m):
                        # if cur says position i,j should be available
                        # but actually it's broken,
                        # then we known this `cur` is invalid, so we skip it
                        # and leave it -1.
                        if nth_bit(cur, j) == 0 and (i, j) in brk:
                            invalid_cur = True
                            break
                    if invalid_cur:
                        continue

                    cnt = 0
                    occupied = [False] * m
                    # claim broken grid is occupied
                    for j in range(m):
                        if (i, j) in brk:
                            occupied[j] = True

                    # then insert vertical dominos to reach state `cur`
                    for j in range(m):
                        if not occupied[j] and nth_bit(s, j) == 0 and nth_bit(cur, j) == 1:
                            cnt += 1
                            occupied[j] = True

                    # and then insert horizontal dominos
                    j = 0
                    while j < m-1:
                        if not occupied[j] and not occupied[j+1] and \
                                nth_bit(cur, j) == 1 and nth_bit(cur, j+1) == 1:
                            occupied[j] = True
                            occupied[j+1] = True
                            j += 2
                            cnt += 1
                        else:
                            j += 1
                    
                    # check invalid cur again
                    for j in range(m):
                        if nth_bit(cur, j) == 1 and not occupied[j]:
                            invalid_cur = True
                            break
                    if invalid_cur:
                        continue

                    next_dp[cur] = max(next_dp[cur], dp[s] + cnt)

            dp = next_dp
        return max(dp)


    @solution
    def domino_dp(self, n, m, broken):
        # 116ms
        # https: // leetcode-cn.com/circle/discuss/1I3IVg/view/kxknaG/
        # m * n * 2^m
        brk = set(tuple(b) for b in broken)
        N = 1 << m
        dp = [-1] * N
        dp[N-1] = 0

        SKIP, HORIZ, VERTI, BROKEN = 0, 1, 2, 4
        def next_state(s, typ):
            # clean highest bit
            s = ~(1 << (m-1)) & s

            if typ == SKIP:  # keep it empty
                return s << 1
            elif typ == HORIZ:  # place horizontal domino
                return ((s | 1) << 1) | 1
            elif typ == VERTI:  # palce a vertical domino
                return (s << 1) | 1
            elif typ == BROKEN:  # broken grid, mark it occupied
                return (s << 1) | 1
            raise ValueError('unrecognized typ')

        for i in range(n):
            for j in range(m):
                next_dp = [-1] * N
                for state in range(N):
                    if dp[state] == -1:
                        continue
                    if (i, j) in brk:
                        s = next_state(state, BROKEN)
                        next_dp[s] = max(next_dp[s], dp[state])
                        continue
                    s = next_state(state, SKIP)
                    next_dp[s] = max(next_dp[s], dp[state])
                    if j > 0 and state & 1 == 0:
                        s = next_state(state, HORIZ)
                        next_dp[s] = max(next_dp[s], dp[state]+1)
                    if i > 0 and state & (1<<(m-1)) == 0:
                        s = next_state(state, VERTI)
                        next_dp[s] = max(next_dp[s], dp[state]+1)
                dp = next_dp

        return max(dp)


    @solution
    def do(self, n, m, broken):
        # solution from https://leetcode-cn.com/u/sleepybag/
        # greedy solution. i don't know how to prove it
        b = [[0 for i in range(m + 2)] for j in range(n + 2)]
        for x, y in broken:
            b[x + 1][y + 1] = 1
        for x in range(0, n + 2):
            b[x][0] = 1
            b[x][-1] = 1
        for y in range(0, m + 2):
            b[0][y] = 1
            b[-1][y] = 1

        def corner(x, y):
            d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            c = 0
            for dx, dy in d:
                if b[x + dx][y + dy]:
                    c += 1
            return c

        def put(x, y):
            b[x][y] = 1
            d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in d:
                if not b[x + dx][y + dy]:
                    b[x + dx][y + dy] = 1
                    break
            return

        ans = 0
        go_on = True
        while go_on:
            go_on = False
            for x in range(n):
                for y in range(m):
                    if not b[x + 1][y + 1]:
                        c = corner(x + 1, y + 1)
                        # dead grid, fill it
                        if c == 4:
                            b[x + 1][y + 1] = 1
                            go_on = True
                        # only one way to place domino, fill it
                        elif c == 3:
                            put(x + 1, y + 1)
                            ans += 1
                            go_on = True

            # don't find top-priority grid, make one here
            if not go_on:
                for x in range(n):
                    for y in range(m):
                        if not go_on and not b[x + 1][y + 1]:
                            c = corner(x + 1, y + 1)
                            if c == 2 or c == 1:
                                put(x + 1, y + 1)
                                ans += 1
                                go_on = True

        return ans




def main():
    q = Q04()
    q.add_args(2, 3, [[1, 0], [1, 1]])
    q.add_args(3, 3, [])
    q.run()


if __name__ == "__main__":
    main()
