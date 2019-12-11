from heapq import heappushpop, heappop, heappush


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.bigheap = []
        self.smallheap = []
        self.n = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.n % 2 == 0:
            x = heappushpop(self.bigheap, num)
            heappush(self.smallheap, -x)
        else:
            x = heappushpop(self.smallheap, -num)
            heappush(self.bigheap, -x)
        self.n += 1


    def findMedian(self):
        """
        :rtype: float
        """
        if self.n == 0:
            return None
        elif self.n % 2 == 0:
            return (self.bigheap[0] - self.smallheap[0]) / 2.0
        else:
            return -self.smallheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

def main():
    medianfinder = MedianFinder()
    operations = ['addNum', 'addNum', 'findMedian', 'addNum', 'findMedian']
    oprands = [[1], [2], [], [3], []]
    for opt, opd in zip(operations, oprands):
        if hasattr(medianfinder, opt):
            print(getattr(medianfinder, opt).__call__(*opd))


if __name__ == '__main__':
    main()
