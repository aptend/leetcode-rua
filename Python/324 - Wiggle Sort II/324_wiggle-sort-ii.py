from leezy import solution, Solution


class Q324(Solution):
    @solution
    def wiggleSort(self, nums):
        # 180ms 93.70%
        # O(n) space
        N = len(nums)
        aux = sorted(nums)
        k = (N-1) // 2  # left median
        for i in range(0, N, 2):
            nums[i] = aux[k]
            k -= 1
        k = N-1
        for i in range(1, N, 2):
            nums[i] = aux[k]
            k -= 1
        return nums


def main():
    q = Q324()
    q.add_case(q.case([1, 5, 1, 1, 6, 4]))
    q.add_case(q.case([1, 3, 2, 2, 3, 1]))
    q.add_case(q.case([4, 5, 5, 6]))
    q.run()


if __name__ == '__main__':
    main()
