from leezy import Solution, solution


"""
How about returning an inverleaving array?
even, odd, even, odd, ... and so forth
[1, 2, 3, 4] -> [2, 1, 4, 3]

one solution:

N = len(A)
i, j = 0, 1
while True:
    while i < N and (i + A[i]) % 2 == 0:
        i += 2
    while j < N and (j + A[j]) % 2 == 0:
        j += 2
    if i < N and j < N:
        A[i], A[j] = A[j], A[i]
        i += 2
        j += 2
    else:
        break
return A
"""


class Q905(Solution):
    @solution
    def sortArrayByParity(self, A):
        # 56ms 98.22%
        N = len(A)
        i, j = 0, N-1
        while True:
            while i < N and A[i] % 2 == 0:
                i += 1
            while j >= 0 and A[j] % 2 == 1:
                j -= 1
            if i >= j:
                break
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        return A


def main():
    q = Q905()
    q.add_args([3, 1, 2, 4])
    q.run()


if __name__ == "__main__":
    main()
