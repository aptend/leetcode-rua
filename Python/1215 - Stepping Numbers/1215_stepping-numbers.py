from leeyzer import Solution, solution

from heapq import heappop, heappush

class Q1215(Solution):
    @solution
    def countSteppingNumbers(self, low, high):
        ans = []
        if low == 0:
            ans.append(0)
        heap = []
        for i in range(1, 10):
            heappush(heap, i)
        while True:
            x = heappop(heap)
            if x > high:
                break
            if x >= low:
                ans.append(x)
            r = x % 10
            if r != 0:
                heappush(heap, x * 10 + r - 1)
            if r != 9:
                heappush(heap, x * 10 + r + 1)
        return ans


def main():
    q = Q1215()
    q.add_args(0, 21)
    q.run()


if __name__ == "__main__":
    main()
