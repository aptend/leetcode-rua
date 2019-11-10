from leezy import Solution, solution


class Q658(Solution):
    @solution
    def findClosestElements(self, arr, k, x):
        lo, hi = 0, len(arr)-1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] >= x:
                hi = mid - 1
            else:
                lo = mid + 1
        lower_bound = lo

        lo, hi = 0, len(arr)-1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] > x:
                hi = mid - 1
            else:
                lo = mid + 1
        higher_bound = lo

        waiting = k - (higher_bound - lower_bound)
        if higher_bound == len(arr):
            return arr[-k:]
        if lower_bound == 0 or waiting < 0:
            return arr[:k]

        i, j = lower_bound-1, higher_bound
        for _ in range(waiting):
            if i < 0:
                j += 1
            elif j >= len(arr):
                i -= 1
            elif x - arr[i] <= arr[j] - x:
                i -= 1
            else:
                j += 1
        return arr[i+1:j]


def main():
    q = Q658()
    q.add_args([1, 2, 3, 4, 5], 4, 3)
    q.add_args([1, 2, 3, 4, 5], 4, -1)
    q.add_args([1, 2, 3, 4, 5], 4, 15)
    q.add_args([1, 2, 2, 4, 5], 2, 4)
    q.run()


if __name__ == "__main__":
    main()
