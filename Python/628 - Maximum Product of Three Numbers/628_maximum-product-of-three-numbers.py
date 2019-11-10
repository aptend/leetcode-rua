from leezy import Solution, solution
import heapq

class Q628(Solution):
    @solution
    def maximumProduct(self, nums):
        # 268ms 14.65%
        # hah, what a joke
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        p = sorted((x for x in nums if x >= 0), reverse=True)
        n = sorted(x for x in nums if x < 0)
        ans = float('-inf')
        len_p = len(p)
        len_n = len(n)
        if len_p >= 3:
            ans = max(ans, p[0]*p[1]*p[2])
        if len_p >= 1 and len_n >= 2:
            ans = max(ans, p[0]*n[0]*n[1])
        if len_p == 0:
            ans = max(ans, n[-1]*n[-2]*n[-3])
        return ans

    @solution
    def maximum_product(self, nums):
        A = sorted(nums)
        return max(A[-1]*A[-2]*A[-3], A[0]*A[1]*A[-1])
    
    @solution
    def maximum_product_heap(self, nums):
        A, B = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(A[0]*A[1]*A[2], A[0]*B[0]*B[1])
def main():
    q = Q628()
    q.add_args([1, 2, 3])
    q.add_args([1, -2, 3, 4])
    q.add_args([-1, -2, -3, -4])
    q.add_args([-1, -2, 0, -4])
    q.run()


if __name__ == "__main__":
    main()
