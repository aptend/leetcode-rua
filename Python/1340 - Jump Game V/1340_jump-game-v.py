from leezy import solution, Solution


class Q1340(Solution):
    @solution
    def maxJumps(self, arr, d):
        # 536 ms, 90.51%
        N = len(arr)
        arr_idx = sorted(list(range(N)), key=lambda x: arr[x])
        ans = [1] * N
        for i in arr_idx:
            l_max = 0
            for l in range(i-1, max(-1, i-d-1), -1):
                if arr[l] >= arr[i]:
                    break
                l_max = max(l_max, ans[l])
            r_max = 0
            for r in range(i+1, min(N, i+1+d)):
                if arr[r] >= arr[i]:
                    break
                r_max = max(r_max, ans[r])
            ans[i] += max(l_max, r_max)
        return max(ans)


def main():
    q = Q1340()
    q.add_case(q.case([6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], 2).assert_equal(4))
    q.add_case(q.case([3, 3, 3, 3], 3).assert_equal(1))
    q.add_case(q.case([7, 6, 5, 4, 3, 2, 1], 1).assert_equal(7))
    q.add_case(q.case([7, 1, 7, 1, 7, 1], 2).assert_equal(2))
    q.add_case(q.case([66], 1).assert_equal(1))
    q.run()


if __name__ == '__main__':
    main()
