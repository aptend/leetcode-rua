from leeyzer import Solution, solution


class Q1200(Solution):
    @solution
    def minimumAbsDifference(self, arr):
        # 412ms
        arr = sorted(arr)
        diff = min(y-x for x, y in zip(arr, arr[1:]))
        return [[x, y] for x, y in zip(arr, arr[1:]) if y - x == diff]


def main():
    q = Q1200()
    q.add_args([4, 2, 1, 3])
    q.run()


if __name__ == "__main__":
    main()
