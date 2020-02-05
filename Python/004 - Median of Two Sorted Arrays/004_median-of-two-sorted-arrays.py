from leezy import solution, Solution

class Q004(Solution):

    @solution
    def media_reivew(self, nums1, nums2):
        # 76ms 77.18%
        A, B = nums1, nums2
        n1, n2 = len(A), len(B)
        def find_kth(k):
            lo, hi = 0, min(n1-1, k-1)
            while lo <= hi:
                a = (lo + hi) // 2  # A[a]选定大堆第一个
                b = k - a  # b = 0, k个小数全部从A中拿取，增大a跳出循环, 使得lo=k
                           # b > n2, a太小了，B不够取
                if 0 < b <= n2 and A[a] >= B[b-1]:
                    hi = a - 1
                else:
                    lo = a + 1
            if lo == 0:
                return B[k-1]
            elif k-lo == 0:
                return A[k-1]
            else:
                return max(A[lo-1], B[k-lo-1])
        N = n1 + n2
        half = N // 2
        if N % 2 == 0:
            return (find_kth(half) + find_kth(half+1)) * 0.5
        else:
            return find_kth(half+1)

    @solution
    def median(self, nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.median(nums2, nums1)
        if n2 == 0:
            return None
        k = (n1+n2-1) // 2
        lo, hi = 0, n1-1
        while lo <= hi:
            m1 = lo + (hi-lo) // 2
            m2 = k - m1
            if m2 == 0 or nums1[m1] >= nums2[m2-1]:
                hi = m1 - 1
            else:
                lo = m1 + 1

        candidates = [nums2[k-lo]]
        if n1 > 0 and lo < n1:
            candidates.append(nums1[lo])
            if lo < n1 - 1:
                candidates.append(nums1[lo+1])
        if k-lo < n2 - 1:
            candidates.append(nums2[k-lo+1])
        candidates.sort()
        if (n1+n2) % 2 == 1:
            return candidates[0]
        else:
            return sum(candidates[:2]) * 0.5



def main():
    q = Q004()
    q.add_case(q.case([1, 3], [2]).assert_equal(2.0))
    q.add_case(q.case([1, 2], [-1, 3]).assert_equal(1.5))
    q.add_case(q.case([1, 2], [3, 4]).assert_equal(2.5))
    q.add_case(q.case([1, 2, 3], [4, 5, 6]).assert_equal(3.5))
    q.add_case(q.case([3, 4], []).assert_equal(3.5))
    q.add_case(q.case([1, 2, 3], [1, 2, 2]).assert_equal(2.0))
    q.add_case(q.case([1, 2], [3, 4]).assert_equal(2.5))
    q.add_case(q.case([9, 10, 11, 12], [1, 2, 3, 4]).assert_equal(6.5))
    q.add_case(q.case([1, 3], [2]).assert_equal(2.0))
    q.add_case(q.case([2, 2, 2], [1, 1, 1]).assert_equal(1.5))
    q.add_case(q.case([2, 4, 6, 7], [1, 3, 5, 8, 9]).assert_equal(5))
    q.run()

if __name__ == '__main__':
    main()
