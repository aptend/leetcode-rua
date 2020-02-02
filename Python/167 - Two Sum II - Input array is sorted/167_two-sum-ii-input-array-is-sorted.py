from leezy import solution, Solution


class Q167(Solution):
    @solution
    def twoSum(self, numbers, target):
        # 64ms 70%
        # same with problem 001
        N = len(numbers)
        indices = list(range(N))
        i, j = 0, N-1
        while i < j:
            s = numbers[indices[i]] + numbers[indices[j]]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return [indices[i]+1, indices[j]+1]
        raise RuntimeError('unreachable here')


def main():
    q = Q167()
    q.add_case(q.case([2, 7, 11, 15], 9).assert_equal([1, 2]))
    q.run()

if __name__ == '__main__':
    main()
