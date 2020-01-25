from leezy import solution, Solution

class Q015(Solution):
    @solution
    def threeSum(self, nums):
        # 764ms 79.66%
        nums = sorted(nums)
        target = 0
        N = len(nums)
        ans = []
        for k, c in enumerate(nums):
            if c > target:
                break
            if k > 0 and c == nums[k-1]:
                continue
            i, j = k + 1, N - 1
            while i < j:
                a, b = nums[i], nums[j]
                if a + b > target-c:
                    j -= 1
                elif a + b < target-c:
                    i += 1
                else:
                    ans.append([nums[k], a, b])
                    while i < j and nums[j] == b:
                        j -= 1
                    while i < j and nums[i] == a:
                        i += 1
        return ans



def main():
    q = Q015()
    q.add_case(q.case([-1, 0, 1, 2, -1, -4]))
    q.add_case(q.case([1, 2, -2, -1]))
    q.add_case(q.case([0, 0, 0, 0, 0]))
    q.add_case(q.case([-1, -1, 0, 0, 0, 0, 0, 1, 1]))
    q.run()

if __name__ == '__main__':
    main()
