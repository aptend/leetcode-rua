from leezy import solution, Solution


class Q1103(Solution):
    @solution
    def distributeCandies(self, candies, num_people):
        # 32ms 91.14%
        n = num_people
        base = (n + 1) * n // 2
        diff = n * n

        k = 1
        cnt = base
        while cnt < candies:
            cnt += base + k * diff
            k += 1

        k = k - 1
        ans = [0] * n
        if k > 0:
            for i in range(n):
                ans[i] = k * (i*2 + 2 + n * (k-1)) // 2

        left_c = candies - sum(ans)
        need = 1 + n * k
        for i in range(n):
            if left_c >= need:
                ans[i] += need
                left_c -= need
                need += 1
            else:
                ans[i] += left_c
                break
        return ans


def main():
    q = Q1103()
    q.add_case(q.case(7, 4).assert_equal([1, 2, 3, 1]))
    q.add_case(q.case(10, 3).assert_equal([5, 2, 3]))
    q.add_case(q.case(57, 2).assert_equal([27, 30]))
    q.run()


if __name__ == '__main__':
    main()
