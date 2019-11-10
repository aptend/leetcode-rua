from leezy import solution, Solution

class Q1243(Solution):
    @solution
    def transformArray(self, arr):
        ans = arr[:]
        stop = False
        N = len(arr)
        while not stop:
            nxt = ans[:]
            stop = True
            for i in range(1, N-1):
                if ans[i-1] < ans[i] > ans[i+1]:
                    nxt[i] -= 1
                    stop = False
                elif  ans[i-1] > ans[i] < ans[i+1]:
                    nxt[i] += 1
                    stop = False
            ans = nxt
        return ans


def main():
    q = Q1243()
    q.add_args([6, 2, 3, 4])
    q.run()

if __name__ == '__main__':
    main()
