from leeyzer import solution, Solution

from collections import Counter

class Q169(Solution):
    @solution
    def majorityElement(self, nums):
        # 196ms 71.76%
        return Counter(nums).most_common(1)[0][0]
    
    @solution
    def majority_element(self, nums):
        # 212ms
        # kind of dp
        # when count == 0, means nums[..i] has no majority
        # and the problem is reduced to subproblem of nums[i+1..]
        cand, count = nums[0], 1
        for x in nums[1:]:
            if x == cand:
                count += 1
            else:
                count -= 1
            if count == 0:
                cand, count = x, 1
        return cand


def main():
    q = Q169()
    q.add_args([3, 2, 3])
    q.add_args([1, 1, 3, 3, 2, 3])
    q.run()

if __name__ == '__main__':
    main()
