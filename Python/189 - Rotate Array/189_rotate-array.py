from leezy import solution, Solution
from collections import deque

class Q189(Solution):
    @solution
    def rotate(self, nums, k):
        # 64ms 89.44ms O(1) space
        # same wiht 1260 shift 2d grid
        N = len(nums)
        def rot(i):
            s = (i + k) % N
            prev = nums[i]
            while s != i:
                tmp = nums[s]
                nums[s] = prev
                prev = tmp
                s = (s + k) % N
            nums[i] = prev

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        for i in range(gcd(k, N)):
            rot(i)
        return nums
    
    @solution
    def rotate_deque(self, nums, k):
        q = deque(nums)
        q.rotate(k)
        nums[:] = q
        return nums




def main():
    q = Q189()
    q.add_case(q.case([1, 2, 3, 4, 5, 6, 7], 3))
    q.add_case(q.case([1, 2, 3, 4, 5, 6], 2))
    q.run()

if __name__ == '__main__':
    main()
