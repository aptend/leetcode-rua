class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # 68ms 71.04%
        self.accum = [0] * (len(nums)+1)
        for i, x in enumerate(nums, 1):
            self.accum[i] = self.accum[i-1]+x

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.accum[j+1] - self.accum[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
def main():
    numarray = NumArray([-2, 0, 3, -5, 2, -1])
    operations = ['sumRange', 'sumRange', 'sumRange']
    operands = [[0, 2], [2, 5], [0, 5]]
    for opt, opd in zip(operations, operands):
        if hasattr(numarray, opt):
            print(getattr(numarray, opt).__call__(*opd))


if __name__ == "__main__":
    main()
