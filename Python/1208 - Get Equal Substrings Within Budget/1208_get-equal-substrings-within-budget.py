from leezy import Solution, solution


class Q1208(Solution):
    @solution
    def equalSubstring(self, s, t, maxCost):
        # 96ms
        A = [abs(ord(x) - ord(y)) for x, y in zip(s, t)]
        i = j = 0
        N = len(A)
        ans = 0
        sum_ = 0
        while j < N:
            sum_ += A[j]
            j += 1
            if sum_ <= maxCost:
                ans = max(ans, j - i)
            while sum_ > maxCost:
                sum_ -= A[i]
                i += 1
        return ans


def main():
    q = Q1208()
    q.add_args('abcd', 'bcdf', 3)
    q.run()


if __name__ == "__main__":
    main()
