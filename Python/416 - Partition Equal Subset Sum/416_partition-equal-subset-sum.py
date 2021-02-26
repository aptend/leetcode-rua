from leezy import Solution, solution


class Q416(Solution):
    @solution
    def canPartition(self, nums):
        # see 494. target sum for more infomation
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = [False] * (target+1)
        dp[0] = True
        for n in nums:
            for i in range(target, n-1, -1):
                dp[i] |= dp[i-n]
        return dp[target]

    @solution
    def can_partition(self, nums):
        # 96.47%
        K = sum(nums)
        if K % 2 == 1:
            return False
        K = K // 2
        cur_set = set()
        nxt_set = set()
        cur_set.add(0)
        for n in nums:
            for x in cur_set:
                nxt_set.add(x + n)
            cur_set |= nxt_set
            # stop early
            if K in cur_set:
                return True
            nxt_set.clear()
        return False


def main():
    q = Q416()
    q.add_case(q.case([1, 5, 11, 5]))
    q.add_case(q.case([1, 2, 3, 5]))
    q.run()


if __name__ == "__main__":
    main()
