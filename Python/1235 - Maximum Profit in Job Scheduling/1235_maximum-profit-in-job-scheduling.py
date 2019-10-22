from leeyzer import solution, Solution

from bisect import bisect_right

class Q1235(Solution):
    @solution
    def jobScheduling(self, startTime, endTime, profit):
        # 656ms
        N = len(startTime)
        zone = sorted([(s, e, p) for s, e, p in zip(startTime, endTime, profit)], key = lambda x: x[1])
        ends = sorted(endTime)
        prev = []
        for i in range(N):
            idx = bisect_right(ends, zone[i][0])
            if idx == 0:
                prev.append(-1)
            else:
                prev.append(idx-1)
        result = [0] * (N+1)
        for i in range(N):
            if prev[i] == -1:
                result[i] = max(result[i-1], zone[i][2])
            else:
                result[i] = max(result[prev[i]] + zone[i][2], result[i-1])
        return max(result)



def main():
    q = Q1235()
    q.add_args([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70])
    q.run()

if __name__ == '__main__':
    main()
