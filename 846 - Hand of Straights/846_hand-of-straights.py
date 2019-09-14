from leeyzer import Solution, solution

from collections import Counter

class Q846(Solution):
    @solution
    def isNStraightHand(self, hand, W):
        # 228ms 68.08%
        if len(hand) % W != 0:
            return False
        cnter = Counter(hand)
        for i in sorted(cnter):
            if cnter[i] == 0:
                continue
            n = cnter[i]
            for j in range(i, i+W):
                if j not in cnter or cnter[j] < cnter[i]:
                    return False
                cnter[j] -= n
        return True



def main():
    q = Q846()
    q.add_args([1, 2, 3, 4, 5, 6], 2)
    q.add_args([1, 2, 3, 6, 2, 3, 4, 7, 8], 3)
    q.add_args([1, 2, 3, 4, 5], 4)
    q.run()


if __name__ == "__main__":
    main()
