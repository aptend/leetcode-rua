from leezy import Solution, solution


class Q670(Solution):
    @solution
    def maximumSwap(self, num):
        # 8ms 97.85%
        nums = list(str(num))
        N = len(nums)
        greater = [None] * N
        max_ = N-1
        for i in range(N-1, -1, -1):
            if nums[i] > nums[max_]:
                max_ = i
            greater[i] = max_
        for i in range(N):
            if nums[i] != nums[greater[i]]:
                j = greater[i]
                nums[i], nums[j] = nums[j], nums[i]
                return int(''.join(nums))
        return num


def main():
    q = Q670()
    q.add_args(2736)
    q.run()


if __name__ == "__main__":
    main()
