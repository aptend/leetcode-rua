from leezy import solution, Solution


class Q096(Solution):
    @solution
    def numTrees(self, n):
        A = [1]
        for i in range(n):
            kinds = 0
            for j in range(i+1):
                kinds += A[j] * A[i-j]
            A.append(kinds)
        return A[-1]

    @solution
    def num_trees(self, n):
        # Catalan numbers: C(n) = binomial(2n, n)/(n+1) = (2n)!/ (n!(n+1)!).
        # Also called Segner numbers.
        # 1 1 2 5 14 42 132
        ans = 1
        for i in range(n):
            ans *= 2 * (2*i + 1) / (i + 2)
        return int(ans)


def main():
    q = Q096()
    q.add_case(q.case(3))
    q.add_case(q.case(4))
    q.add_case(q.case(5))
    q.run()


if __name__ == '__main__':
    main()
