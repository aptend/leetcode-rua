from leezy import solution, Solution


class Q440(Solution):
    @solution
    def findKthNumber(self, n, k):
        # 24ms 93.07%
        node = 1
        while k > 1:
            span = 1
            base = node
            count = 0
            while base <= n:
                count += min(span, n - base + 1)
                base *= 10
                span *= 10

            if count >= k:
                k -= 1
                node *= 10
            else:
                k -= count
                node += 1
        return node

    @solution
    def find_kth_number(self, n, k):
        def find(node, k):
            if k <= 1:
                return node
            span = 1
            base = node
            count = 0
            while base <= n:
                count += min(span, n - base + 1)
                base *= 10
                span *= 10
            if count >= k:
                return find(node*10, k-1)
            else:
                return find(node+1, k-count)
        return find(1, k)


def main():
    q = Q440()
    q.add_case(q.case(100, 10).assert_equal(17))
    q.add_case(q.case(1, 1).assert_equal(1))
    q.add_case(q.case(13, 10).assert_equal(6))
    q.add_case(q.case(13, 2).assert_equal(10))
    q.add_case(q.case(243, 200).assert_equal(6))
    q.add_case(q.case(243, 111).assert_equal(199))
    q.add_case(q.case(243, 243).assert_equal(99))
    q.run()

if __name__ == '__main__':
    main()
