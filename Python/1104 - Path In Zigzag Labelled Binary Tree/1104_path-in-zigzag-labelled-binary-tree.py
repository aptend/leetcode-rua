from leezy import solution, Solution


class Q1104(Solution):
    @solution
    def pathInZigZagTree(self, label):
        # 20ms 98.84%
        if label == 1:
            return [1]
        k = 1
        while 1 << k <= label:
            k += 1
        k -= 1  # label is among k level, there are 2 ** k nodes in this level

        ans = []
        if k % 2 == 1:
            total = 1 << k
            n = total + total*2 - 1 - label
        else:
            n = label

        while k >= 0:
            if k % 2 == 1:  # this level is reversed
                total = 1 << k
                ans.append(total*2 - n + total - 1)
            else:
                ans.append(n)
            n //= 2
            k -= 1
        return ans[::-1]


def main():
    q = Q1104()
    q.add_case(q.case(16).assert_equal([1, 3, 4, 15, 16]))
    q.add_case(q.case(14).assert_equal([1, 3, 4, 14]))
    q.add_case(q.case(26).assert_equal([1, 2, 6, 10, 26]))
    q.run()


if __name__ == '__main__':
    main()
