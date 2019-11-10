from leezy import Solution, solution

from collections import Counter, deque

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
    
    @solution
    def is_n_straight_hand(self, hand, W):
        # emm... a bit obscure
        c = Counter(hand)
        start = deque()
        last_checked, opened = -1, 0
        for i in sorted(c):
            # opened means the lowest quantity requirement for current i
            # less than required or not consecutive seq
            if opened > c[i] or opened > 0 and i > last_checked + 1:
                return False
            # start[i] means how many groups of (i, i+1, i+2, ..., i+W-1)
            # this will make a difference after W step
            start.append(c[i] - opened)
            last_checked, opened = i, c[i]
            if len(start) == W:
                # takes away start[0] groups from opened, which decreases the 
                # lowest quantity requirement for next i
                opened -= start.popleft()
        return opened == 0



def main():
    q = Q846()
    q.add_args([1, 2, 3, 4, 5, 6], 2)
    q.add_args([1, 2, 3, 6, 2, 3, 4, 7, 8], 3)
    q.add_args([1, 2, 3, 4, 5], 4)
    q.run()


if __name__ == "__main__":
    main()
