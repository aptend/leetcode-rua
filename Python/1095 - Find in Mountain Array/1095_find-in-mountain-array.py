from leezy import solution, Solution


class Q1095(Solution):
    @solution
    def findInMountainArray(self, target, mountain_arr):
        M = mountain_arr
        lo, hi = 0, M.length() - 1
        peak = peak_idx = None
        while lo <= hi:
            i = (lo + hi) // 2
            l, m, r = M.get(i-1), M.get(i), M.get(i+1)
            if l < m and m > r:
                peak_idx = i
                peak = m
                break
            elif l < m and m < r:
                lo = i
            else:
                hi = i
        else:
            raise ValueError('invalid mountain array')
        if target == peak:
            return peak_idx
        elif target > peak:
            return -1
        else:
            lo, hi = 0, peak_idx-1
            while lo <= hi:
                i = (lo + hi) // 2
                m = M.get(i)
                if m == target:
                    return i
                elif m > target:
                    hi = i - 1
                else:
                    lo = i + 1
            lo, hi = peak_idx+1, M.length() - 1
            while lo <= hi:
                i = (lo + hi) // 2
                m = M.get(i)
                if m == target:
                    return i
                elif m > target:
                    lo = i + 1
                else:
                    hi = i - 1
            return -1




class MArr:
    def __init__(self, arr):
        self.arr = arr
        self.get_cnt = 0

    def get(self, k):
        self.get_cnt += 1
        return self.arr[k]

    def length(self):
        return len(self.arr)


def main():
    q = Q1095()
    q.add_case(q.case(1, MArr([1, 2, 1])).assert_equal(0))
    q.add_case(q.case(3, MArr([1, 2, 3, 4, 5, 3, 1])).assert_equal(2))
    q.add_case(q.case(3, MArr([0, 1, 2, 4, 2, 1])).assert_equal(-1))
    q.run()


if __name__ == '__main__':
    main()
