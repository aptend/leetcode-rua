from leezy import solution, Solution


class Q376(Solution):
    @solution
    def wiggleMaxLength(self, nums):
        # 220ms 5%
        # O(n^2)
        N = len(nums)
        if N <= 1:
            return N
        dp = [[1, 1] for _ in range(N)]
        ans = 1
        for i in range(1, N):
            x = nums[i]
            for j in range(i):
                if x > nums[j]:
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)
                if x < nums[j]:
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)
            ans = max(ans, dp[i][0], dp[i][1])
        return ans

    @solution
    def wiggle_max_length(self, nums):
        # 32ms 93.46%
        N = len(nums)
        if N <= 1:
            return N
        seq = [nums[0]]
        i = 1
        while i < N and nums[i] == nums[0]:
            i += 1
        if i == N:
            return 1
        up = nums[i] > nums[0]
        seq.append(nums[i])
        for k in range(i+1, N):
            if up and nums[k] < seq[-1]:
                up = False
                seq.append(nums[k])
            elif not up and nums[k] > seq[-1]:
                up = True
                seq.append(nums[k])
            else:
                seq[-1] = nums[k]
        return len(seq)


def main():
    q = Q376()
    q.add_case(q.case([1, 7, 4, 9, 2, 5]).assert_equal(6))
    q.add_case(q.case([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]).assert_equal(7))
    q.add_case(q.case([1, 2, 3, 4, 5, 6, 7, 8, 9]).assert_equal(2))
    q.add_case(q.case([0, 93, 55, 40, 46, 69, 51, 68,
                       72, 9, 32, 84, 34]).assert_equal(9))
    q.run()


if __name__ == '__main__':
    main()
