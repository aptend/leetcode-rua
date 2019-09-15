from leeyzer import Solution, solution
from heapq import heappush, heappop

class Q373(Solution):
    @solution
    def kSmallestPairs(self, nums1, nums2, k):
        # 32ms 93.03%
        if not nums1 or not nums2:
            return []
        heap = [(nums1[0]+nums1[0], 0, 0)]

        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heappush(heap, (nums1[i]+nums2[j], i, j))
        ans = []
        while heap and len(ans) < k:
            _, i, j = heappop(heap)
            ans.append([nums1[i], nums2[j]])
            push(i, j+1)
            if j == 0:
                push(i+1, 0)
        return ans


def main():
    q = Q373()
    q.add_args([1, 7, 11], [2, 4, 6], 3)
    q.run()


if __name__ == "__main__":
    main()
