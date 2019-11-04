from collections import Counter
class Leaderboard:

    def __init__(self):
        self.data = Counter()

    def addScore(self, playerId: int, score: int) -> None:
        self.data[playerId] += score

    def top(self, K: int) -> int:
        return sum(x[1] for x in self.data.most_common(K))

    def reset(self, playerId: int) -> None:
        self.data[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)

def main():
    leaderboard = Leaderboard()
    operations = ['Leaderboard', 'addScore', 'addScore', 'addScore', 'addScore', 'addScore', 'top', 'reset', 'reset', 'addScore', 'top']
    oprands = [[], [1, 73], [2, 56], [3, 39], [4, 51], [5, 4], [1], [1], [2], [2, 51], [3]]
    for opt, opd in zip(operations, oprands):
        if hasattr(leaderboard, opt):
            print(getattr(leaderboard, opt).__call__(*opd))


if __name__ == '__main__':
    main()
