from leezy import solution, Solution

from collections import deque

class Q995(Solution):
    @solution
    def minKBitFlips(self, A, K):
        # 892ms 90.79%
        q = deque()
        ans = 0
        for i, b in enumerate(A):
            while q and q[0] + K - 1 < i:
                q.popleft()
            if b == len(q) % 2:
                if i > len(A) - K:
                    return -1
                q.append(i)
                ans += 1
        return ans

    @solution
    def min_k_bit_flips(self, A, K):
        ans = 0
        win_flip_cnt = 0
        N = len(A)
        need_to_shrink = [False] * N
        for i in range(len(A)):
            # A[i-K] has been flipped but we don't need to consider it anymore
            if need_to_shrink[i]:
                win_flip_cnt -= 1
            if win_flip_cnt % 2 == A[i]:
                if i > N - K:
                    return -1
                if i + K < N:
                    # remind the future of ignoring this flip
                    need_to_shrink[i+K] = True
                win_flip_cnt += 1
                ans += 1
        return ans



def main():
    q = Q995()
    q.add_case(q.case([0, 1, 0], 1).assert_equal(2))
    q.add_case(q.case([1, 1, 0], 2).assert_equal(-1))
    q.add_case(q.case([0, 0, 0, 1, 0, 1, 1, 0], 3).assert_equal(3))
    q.run()

if __name__ == '__main__':
    main()
