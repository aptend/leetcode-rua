from leezy import Solution, solution


class Q870(Solution):
    @solution
    def advantageCount(self, A, B):
        # 420ms 94.64%
        N = len(A)
        ans = [-1] * N
        sorted_Bidx = sorted(list(range(N)), key=lambda x: B[x])
        sorted_A = sorted(A)
        i = j = 0
        stash = []
        for i in range(N):
            Bi = sorted_Bidx[j]
            if sorted_A[i] > B[Bi]:
                ans[Bi] = sorted_A[i]
                j += 1
            else:
                stash.append(sorted_A[i])

        for i, x in enumerate(ans):
            if x == -1:
                ans[i] = stash.pop()
        return ans



def main():
    q = Q870()
    q.add_args([2, 7, 11, 15], [1, 10, 4, 11])
    q.run()


if __name__ == "__main__":
    main()
