class StockSpanner:

    def __init__(self):
        self.skip_t = [0]
        self.prices = [float('inf')]

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        i = len(self.prices)-1
        cnt = 1
        while self.prices[i] <= price:
            cnt += i - self.skip_t[i]
            i = self.skip_t[i]
        self.prices.append(price)
        self.skip_t.append(i)
        return cnt


class StockSpannerI:
    def __init__(self):
        self.stack = []
        self.idx = 0

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.idx += 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        self.stack.append((price, self.idx))
        if len(self.stack) > 1:
            return self.idx - self.stack[-2][1]
        else:
            return self.idx


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
def main():
    # stockspanner = StockSpanner()
    stockspanner = StockSpannerI()
    operations = ['StockSpanner', 'next', 'next', 'next', 'next', 'next', 'next', 'next']
    operands = [[], [100], [80], [60], [70], [60], [75], [85]]
    for opt, opd in zip(operations, operands):
        if hasattr(stockspanner, opt):
            print(getattr(stockspanner, opt).__call__(*opd))


if __name__ == "__main__":
    main()
