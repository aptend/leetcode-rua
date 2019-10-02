from leeyzer import Solution, solution


class Q016(Solution):
    @solution
    def threeSumClosest(self, nums, target):
        # 172ms 30.13%
        A = sorted(nums)
        N = len(A)
        delta = float('inf')
        for k in range(2, N):
            i = 0
            j = k - 1
            while i < j:
                s = A[i] + A[j]
                t = target - A[k]
                if s > t:
                    j -= 1
                elif s < t:
                    i += 1
                else:
                    return target
                if abs(s-t) < abs(delta):
                    delta = s - t
        return target + delta


def main():
    q = Q016()
    q.add_args([-1, 2, 1, -4], 1)
    q.run()


if __name__ == "__main__":
    main()
