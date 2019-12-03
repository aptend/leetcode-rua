from leezy import solution, Solution


class Q001(Solution):
    @solution
    def twoSum(self, nums, target):
        hash_table = {}
        for i, x in enumerate(nums):
            another = target - x
            if x in hash_table:
                return [hash_table[x], i]
            else:
                hash_table[another] = i
    
    @solution
    def two_sum(self, nums, target):
        N = len(nums)
        idx = sorted(range(N), key=lambda x: nums[x])
        i, j = 0, N - 1
        while i < j:
            s = nums[idx[i]] + nums[idx[j]]
            if s == target:
                return [idx[i], idx[j]]
            elif s > target:
                j -= 1
            else:
                i += 1


def main():
    q = Q001()
    q.add_case(q.case([2, 7, 11, 15], 9).assert_equal([0, 1]))
    q.add_case(q.case([3, 2, 4], 6).assert_equal([1, 2]))
    q.run()

if __name__ == '__main__':
    main()
