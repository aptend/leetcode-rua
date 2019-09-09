from leeyzer import Solution, solution
from heapq import heappush, heappop

class Q264(Solution):
    @solution
    def nthUglyNumber(self, n):
        # 140ms 87.42%
        nums = [1]
        i2 = i3 = i5 = 0
        for _ in range(n):
            next2 = nums[i2] * 2
            next3 = nums[i3] * 3
            next5 = nums[i5] * 5
            next_ = min(next2, next3, next5)
            nums.append(next_)
            # if next_ == next2 and next_ == next3
            # increase both i2 and i3
            if next_ == next2: i2 += 1
            if next_ == next3: i3 += 1
            if next_ == next5: i5 += 1
        return nums[n-1]
    
    @solution
    def nth_ugly(self, n):
        # 244ms 26.48%
        q = [1]
        for _ in range(n-1):
            x = q[0]
            # eliminate duplicate ugly number
            while q and q[0] == x:
                heappop(q)
            heappush(q, x*2)
            heappush(q, x*3)
            heappush(q, x*5)
        return q[0]



def main():
    q = Q264()
    q.add_args(10)
    q.run()


if __name__ == "__main__":
    main()
