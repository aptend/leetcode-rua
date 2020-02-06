from leezy import solution, Solution


class Q135(Solution):
    @solution
    def candy(self, ratings):
        # 168ms 88.24%
        N = len(ratings)
        candies = [1] * len(ratings)
        for i in range(1, N):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        for i in range(N-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        return sum(candies)


def main():
    q = Q135()
    q.add_case(q.case([1, 0, 2]).assert_equal(5))
    q.add_case(q.case([1, 2, 2]).assert_equal(4))
    q.run()


if __name__ == '__main__':
    main()
