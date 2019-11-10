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


def main():
    q = Q1248()
    q.add_args([1, 1, 2, 1, 1], 3)
    q.run()

if __name__ == '__main__':
    main()
