from leeyzer import Solution, solution


class Q080(Solution):
    @solution
    def removeDuplicates(self, nums):
        # 36ms 88.54%
        pass
        N = len(nums)
        if N <= 2:
            return N
        i = j = 0
        cur = nums[0]
        cnt = 0
        while True:
            while j < N and nums[j] == cur:
                cnt += 1
                j += 1
            for _ in range(min(cnt, 2)):
                nums[i] = cur
                i += 1
            if j >= N:
                break
            cnt = 0
            cur = nums[j]
        return i


def main():
    q = Q080()
    q.add_args([1, 1, 1, 2, 2, 3])
    q.run()


if __name__ == "__main__":
    main()
