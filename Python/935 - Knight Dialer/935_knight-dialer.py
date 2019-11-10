from leezy import Solution, solution


class Q935(Solution):
    @solution
    def knightDialer(self, N):
        # 1004ms 47.75%
        # can be optmized by dismissing `move_map`
        # variables updating can be hard-coded in the loop
        # another point:
        # mod operation can be arbitrarily inserted into a linear computing process 
        # without affecting the final result
        move_map = [
            (4, 6),
            (6, 8),
            (7, 9),
            (4, 8),
            (3, 9, 0),
            (),
            (1, 7, 0),
            (2, 6),
            (1, 3),
            (2, 4)
        ]
        kmod = 1e9 + 7
        dp = [1] * 10
        cur_dp = [0] * 10
        for _ in range(N-1):
            for i in range(10):
                for dest in move_map[i]:
                    cur_dp[dest] = (cur_dp[dest] + dp[i]) % kmod
            cur_dp, dp = dp, cur_dp
            for j in range(10):
                cur_dp[j] = 0
        return int(sum(dp) % kmod)


def main():
    q = Q935()
    q.add_args(1)
    q.add_args(2)
    q.add_args(3)
    q.run()


if __name__ == "__main__":
    main()
