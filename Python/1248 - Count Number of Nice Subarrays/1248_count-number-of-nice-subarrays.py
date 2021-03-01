from leezy import solution, Solution


class Q1248(Solution):
    @solution
    def numberOfSubarrays(self, nums, k):
        # 1116ms 20%
        # same 0992_subarrays_with_k_different_integers
        N = len(nums)

        def at_most(k):
            i = 0
            odd_count = 0
            sub_count = 0
            for j in range(N):
                if nums[j] % 2 == 1:
                    odd_count += 1
                while odd_count > k:
                    if nums[i] % 2 == 1:
                        odd_count -= 1
                    i += 1
                sub_count += j - i + 1
            return sub_count
        return at_most(k) - at_most(k-1)

    @solution
    def number_of_subarrays(self, nums, k):
        # time used & rank: 256 ms faster than 29.66%
        # memory used & rank: 20.9 MB less than 6.78%
        # reduce to 560 - subarray sum equals k
        nums = [n % 2 for n in nums]
        memo = {0: 1}
        accum = 0
        ans = 0
        for i in nums:
            accum += i
            if accum - k in memo:
                ans += memo[accum - k]
            if accum in memo:
                memo[accum] += 1
            else:
                memo[accum] = 1
        return ans


def main():
    q = Q1248()
    q.add_case(q.case([1, 1, 2, 1, 1], 3).assert_equal(2))
    q.add_case(q.case([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2).assert_equal(16))
    q.run()


if __name__ == '__main__':
    main()
