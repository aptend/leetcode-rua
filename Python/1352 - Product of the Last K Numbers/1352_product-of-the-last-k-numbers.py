
class ProductOfNumbers:
    # 280 ms, 92.70%
    def __init__(self):
        self.acc = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.acc.clear()
            self.acc.append(1)
        else:
            self.acc.append(self.acc[-1] * num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k >= len(self.acc):
            return 0
        return self.acc[-1] // self.acc[-k-1]


def main():
    productofnumbers = ProductOfNumbers()
    operations = ['add', 'add', 'add', 'add', 'add', 'getProduct', 'getProduct', 'getProduct', 'add', 'getProduct']
    oprands = [[3], [0], [2], [5], [4], [2], [3], [4], [8], [2]]
    for opt, opd in zip(operations, oprands):
        if hasattr(productofnumbers, opt):
            print(getattr(productofnumbers, opt).__call__(*opd))


if __name__ == '__main__':
    main()
