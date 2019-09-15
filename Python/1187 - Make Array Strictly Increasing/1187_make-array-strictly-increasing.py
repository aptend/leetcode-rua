from leeyzer import Solution, solution

from bisect import bisect_right
from collections import defaultdict
class Q1187(Solution):
    @solution
    def makeArrayIncreasing(self, arr1, arr2):
        # 796ms 76.99%
        arr2 = sorted(arr2)
        dp = {-1: 0}
        # len(dp) is at most 2
        for x in arr1:
            new_dp = defaultdict(lambda: float('inf'))
            for key, val in dp.items():
                # if x can be appended to arr1 to make it still increasing
                if x > key:
                    new_dp[x] = min(new_dp[x], val)
                # try to find a minimum value in arr2 to expand arr1
                # minimum value won't affect following operation
                i = bisect_right(arr2, key)
                if i < len(arr2):
                    y = arr2[i]
                    new_dp[y] = min(new_dp[y], val+1)
            if len(new_dp) == 0:
                return -1
            dp = new_dp
        return min(dp.values())


def main():
    q = Q1187()
    q.add_args([1, 5, 3, 6, 7], [1, 3, 2, 4])
    q.add_args([1, 5, 3, 6, 7], [1, 3, 4])
    q.add_args([1, 5, 3, 6, 7], [1, 3, 6, 6])
    q.run()


if __name__ == "__main__":
    main()
