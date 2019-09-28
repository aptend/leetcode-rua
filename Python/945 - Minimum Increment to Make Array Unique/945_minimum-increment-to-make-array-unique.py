from leeyzer import Solution, solution


class Q945(Solution):
    @solution
    def minIncrementForUnique(self, A):
        # 384ms 74.70%
        A = sorted(A)
        hold = -1
        ans = 0
        for x in A:
            if x > hold:
                hold = x
            else:
                ans += hold - x + 1
                hold += 1
        return ans


def main():
    q = Q945()
    q.add_args([1, 2, 2])
    q.add_args([0, 0, 2, 2])
    q.add_args([3, 2, 1, 2, 1, 7])
    q.run()


if __name__ == "__main__":
    main()
