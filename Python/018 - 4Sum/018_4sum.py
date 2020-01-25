from leezy import solution, Solution
from collections import defaultdict, Counter
from bisect import bisect_left
class Q018(Solution):
    @solution
    def fourSum(self, nums, target):
        # 2156 ms, 5.05%
        ans = set()
        nums = sorted(nums)
        N = len(nums)
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    t = target - nums[i] - nums[j] - nums[k]
                    idx = bisect_left(nums, t, k+1, N)
                    if idx < N and nums[idx] == t:
                        ans.add((nums[i], nums[j], nums[k], t))
        return ans

    @solution
    def four_sum(self, nums, target):
        # 392ms 57.07%
        nums = sorted(nums)
        if target > 0 and target > 4 * nums[-1]:
            return []
        if target < 0 and target < 4 * nums[0]:
            return []
        N = len(nums)
        ans = []
        for m in range(N):
            a = nums[m]
            if m > 0 and (a == nums[m-1]):
                continue
            for n in range(m+1, N):
                b = nums[n]
                if n > m+1 and (b == nums[n-1]):
                    continue
                i, j = n + 1, N - 1
                while i < j:
                    c, d = nums[i], nums[j]
                    if c + d > target-a-b:
                        j -= 1
                    elif c + d < target-a-b:
                        i += 1
                    else:
                        ans.append([a, b, c, d])
                        while i < j and nums[j] == d:
                            j -= 1
                        while i < j and nums[i] == c:
                            i += 1
        return ans

    @solution
    def four_sum_ultra(self, nums, target):
        # 84ms 92.73%
        def collect_n_sum(lo, n, target, formed, ans):
            if lo >= len(nums) or target < nums[lo] * n or target > nums[-1] * n:
                return
            if n == 2:
                i, j = lo, len(nums)-1
                while i < j:
                    a, b = nums[i], nums[j]
                    if a + b > target:
                        j -= 1
                    elif a + b < target:
                        i += 1
                    else:
                        ans.append(formed + [a, b])
                        while i < j and nums[i] == a:
                            i += 1
                        while i < j and nums[j] == b:
                            j -= 1
            else:
                for k in range(lo, len(nums)):
                    if k > lo and nums[k] == nums[k-1]:
                        continue
                    formed.append(nums[k])
                    collect_n_sum(k+1, n-1, target-nums[k], formed, ans)
                    formed.pop()
        nums = sorted(nums)
        formed, ans = [], []
        collect_n_sum(0, 4, target, formed, ans)
        return ans


def main():
    q = Q018()
    q.add_case(q.case([1, 0, -1, 0, -2, 2], 0))
    q.add_case(q.case([1, 1, -1, -1, -1, 1], 0))
    q.add_case(q.case([-1, 0, 1, 2, -1, -4], -1))
    q.run()

if __name__ == '__main__':
    main()
