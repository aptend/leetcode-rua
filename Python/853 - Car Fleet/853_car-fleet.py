from leeyzer import Solution, solution


class Q853(Solution):
    @solution
    def carFleet(self, target, position, speed):
        # 200ms 92.62% Python3
        N = len(position)
        time_cost = [(target - position[i]) / speed[i] for i in range(N)]
        priority = sorted(range(N), key=lambda x: position[x], reverse=True)
        max_time = 0
        ans = 0
        for p in priority:
            if time_cost[p] > max_time:
                ans += 1
                max_time = time_cost[p]
        return ans


def main():
    q = Q853()
    q.add_args(12, [], [])
    q.add_args(10, [6, 8], [3, 2])
    q.add_args(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])
    q.add_args(12, [10, 8, 0, 5, 3], [2, 4, 10, 1, 3])
    q.run()


if __name__ == "__main__":
    main()
