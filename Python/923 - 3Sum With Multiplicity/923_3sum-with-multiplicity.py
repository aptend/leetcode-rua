from leeyzer import Solution, solution

from collections import Counter
import itertools


class Q923(Solution):
    @solution
    def threeSumMulti(self, A, target):
        # 92ms 77.08%
        cnt = Counter(A)
        ans = 0
        B = list(sorted(cnt.keys()))
        N = len(B)
        for k in range(N):
            # use only one B[k]
            i = 0
            j = k - 1
            while i < j:
                s = B[i] + B[j]
                t = target - B[k]
                if s > t:
                    j -= 1
                elif s < t:
                    i += 1
                else:
                    ans += cnt[B[i]] * cnt[B[j]] * cnt[B[k]]
                    i += 1
                    j -= 1

            # all three are B[k]
            n = cnt[B[k]]
            if 3 * B[k] == target:
                ans += n * (n-1) * (n-2) // 6
            # use two B[k]
            elif target - B[k] * 2 in cnt:
                ans += cnt[target - B[k] * 2] * (n * (n-1) // 2)
        return ans % (10**9 + 7)

    @solution
    def three_sum(self, A, target):
        # 96ms
        c = Counter(A)
        res = 0
        for i, j in itertools.combinations_with_replacement(c, 2):
            k = target - i - j
            if i == j == k:
                res += c[i] * (c[i] - 1) * (c[i] - 2) // 6
            elif i == j != k:
                res += c[i] * (c[i] - 1) // 2 * c[k]
            elif k > i and k > j:
                res += c[i] * c[j] * c[k]
        return res % (10**9 + 7)


def main():
    q = Q923()
    q.add_args([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8)
    q.add_args([1, 1, 2, 2, 2, 2], 5)
    q.add_args([0, 0, 0], 0)
    q.add_args([2, 3, 3, 1, 0, 0, 1], 5)
    q.add_args([52, 53, 86, 11, 35, 1, 41, 34, 52, 64, 90, 54, 84, 99,
                67, 8, 80, 100, 51, 66, 37, 31, 13, 13, 22, 31, 81, 96, 81, 96], 79)
    q.run()


if __name__ == "__main__":
    main()
