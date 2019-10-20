from leeyzer import solution, Solution

class Q1230(Solution):
    @solution
    def probabilityOfHeads(self, prob, target):
        # 568ms
        dp = [0] * (target + 1)
        dp[0] = 1
        new_dp = dp[:]
        for i, p in enumerate(prob, 1):
            new_dp[0] = dp[0] * (1-p)
            for k in range(1, min(i+1, target+1)):
                new_dp[k] = dp[k] * (1-p) + dp[k-1] * p
            dp, new_dp = new_dp, dp
        return dp[target]


def main():
    q = Q1230()
    q.add_args([0.4], 1)
    q.add_args([0.5,0.5,0.5,0.5,0.5], 0)
    q.run()

if __name__ == '__main__':
    main()
