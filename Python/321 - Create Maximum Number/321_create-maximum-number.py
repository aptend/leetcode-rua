from leezy import solution, Solution


class Q321(Solution):
    @solution
    def maxNumber(self, nums1, nums2, k):
        # 484ms 52.40%
        def max_solo_k(nums, k):
            to_pop = len(nums) - k
            stack = []
            for x in nums:
                while stack and stack[-1] < x and to_pop > 0:
                    stack.pop()
                    to_pop -= 1
                stack.append(x)
            return stack[:k]

        def max_merged(nums1, nums2):
            merged = []
            i = j = 0
            while i < len(nums1) and j < len(nums2):
                if nums1[i:] > nums2[j:]:
                    merged.append(nums1[i])
                    i += 1
                else:
                    merged.append(nums2[j])
                    j += 1
            if i == len(nums1):
                merged.extend(nums2[j:])
            else:
                merged.extend(nums1[i:])
            return merged
        
        ans = []
        # pick i elements from nums1, k - i ones from nums2
        n1, n2 = len(nums1), len(nums2)
        for i in range(max(0, k-n2), min(k, n1)+1):
            ans = max(ans, max_merged(max_solo_k(nums1, i), max_solo_k(nums2, k-i)))
        return ans


def main():
    q = Q321()
    q.add_case(q.case([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5).assert_equal( [9, 8, 6, 5, 3]))
    q.add_case(q.case([6, 7], [6, 0, 4], 5).assert_equal([6, 7, 6, 0, 4]))
    q.add_case(q.case([3, 9], [8, 9], 3).assert_equal([9, 8, 9]))
    q.run()


if __name__ == '__main__':
    main()
