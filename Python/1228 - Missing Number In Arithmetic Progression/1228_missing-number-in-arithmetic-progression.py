from leezy import solution, Solution

class Q1228(Solution):
    @solution
    def missingNumber(self, arr):
        # 56ms
        # solution from lee215
        # complete arr has n + 1 items
        return (arr[0] + arr[-1]) * (len(arr) + 1) // 2 - sum(arr)
    
    @solution
    def missing_number(self, arr):
        # 56ms
        # my own original idea
        # determine the true diff by inspecting first diff
        d1 = arr[1] - arr[0]
        d2 = arr[2] - arr[1]
        N = len(arr)
        if d1 == d2:
            for i in range(2, N-1):
                if arr[i+1] - arr[i] != d1:
                    return arr[i] + d1
        if abs(d1) < abs(d2):
            return arr[1] + d1
        else:
            return arr[0] + d2


def main():
    q = Q1228()
    q.add_args([5, 7, 11, 13])
    q.add_args([5, 5, 5])
    q.add_args([1, 2, 4])
    q.add_args([15, 13, 12])
    q.run()

if __name__ == '__main__':
    main()
