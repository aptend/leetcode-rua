from leeyzer import Solution, solution
from bisect import bisect_right

class Q825(Solution):
    @solution
    def numFriendRequests(self, ages):
        # 448ms 26.48%
        ages = sorted(ages)
        cnt = 0
        for x in ages:
            i = bisect_right(ages, x // 2 + 7)
            j = bisect_right(ages, x)
            if j > i:
                cnt += j - i - 1
        return cnt



def main():
    q = Q825()
    q.add_args([16, 16])
    q.run()


if __name__ == "__main__":
    main()
