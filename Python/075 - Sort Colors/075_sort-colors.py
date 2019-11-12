from leezy import solution, Solution

from collections import Counter

class Q075(Solution):
    @solution
    def sortColors(self, nums):
        # 44ms 32.93%
        counter = Counter(nums)
        i = 0
        for key in [0, 1, 2]:
            for j in range(i, i+counter[key]):
                nums[j] = key
            i += counter[key]
        return nums

    @solution
    def sort_colors(self, nums):
        # 32ms 95.60%
        # 3-way partition
        i = k = 0
        j = len(nums) - 1
        while k <= j:
            if nums[k] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
                k += 1
            elif nums[k] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                j -= 1
            else:
                k += 1
        return nums


def main():
    q = Q075()
    q.add_case(q.case([2, 0, 2, 1, 1, 0]).assert_equal([0, 0, 1, 1, 2, 2]))
    q.run()

if __name__ == '__main__':
    main()
