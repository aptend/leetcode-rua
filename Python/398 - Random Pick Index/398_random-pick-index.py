
from random import randint


class Q398:
    # 316ms 71.48%
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        cnt = 0
        idx = None
        for i, x in enumerate(self.nums):
            if x == target:
                if randint(0, cnt) == 0:
                    idx = i
                cnt += 1
        return idx


def main():
    q = Q398([2])
    print([q.pick(2) for _ in range(5)])


if __name__ == '__main__':
    main()
