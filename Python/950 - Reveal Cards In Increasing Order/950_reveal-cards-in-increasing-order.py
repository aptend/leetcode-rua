from leezy import Solution, solution

from collections import deque


class Q950(Solution):
    @solution
    def deckRevealedIncreasing(self, deck):
        # 52ms 90.11%
        # according to Master Theorem
        # a = 1, b = 2, f(n) = n
        # we can find such k < 1 that n/2 < kn, so `reveal` is O(n)
        def reveal(deck):
            if len(deck) == 1:
                return deck
            aux = deck[:]
            j = 0
            for i in range(0, len(deck), 2):
                aux[i] = deck[j]
                j += 1
            # the scale of the problem is halved
            inner_deck = deque(reveal(deck[j:]))
            inner_deck.rotate(j)
            for i, x in enumerate(inner_deck, 1):
                aux[i*2-1] = x
            return aux
        deck = sorted(deck)
        return reveal(deck)

    @solution
    def deck_reveal(self, deck):
        # 64ms
        # this solution focuses the position
        N = len(deck)
        q = deque(range(N))
        ans = [0] * N
        for card in sorted(deck):
            ans[q.popleft()] = card
            # rotate left, front element goes to back end
            q.rotate(-1)
        return ans


def main():
    q = Q950()
    q.add_case(q.case([17, 13, 11, 2, 3, 5, 7])
                .assert_equal([2, 13, 3, 11, 5, 17, 7]))
    q.add_case(q.case([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
                .assert_equal([1, 9, 2, 7, 3, 11, 4, 8, 5, 10, 6]))
    q.run()


if __name__ == "__main__":
    main()
