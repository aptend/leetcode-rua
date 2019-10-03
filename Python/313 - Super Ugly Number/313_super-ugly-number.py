from leeyzer import Solution, solution

from heapq import heappop, heappush

class Q313(Solution):
    @solution
    def nthSuperUglyNumber(self, n, primes):
        # 276ms 96.48ms like 264
        ugly = [1]
        heap = []
        for p in primes:
            heappush(heap, (p, p, 0))
        cnt = 1
        while cnt < n:
            v, p, idx = heappop(heap)
            if v > ugly[-1]:
                ugly.append(v)
                cnt += 1
            heappush(heap, (p * ugly[idx+1], p, idx+1))
        return ugly[-1]


def main():
    q = Q313()
    q.add_args(12, [2, 7, 13, 19])
    q.add_args(11, [7])
    q.run()


if __name__ == "__main__":
    main()
