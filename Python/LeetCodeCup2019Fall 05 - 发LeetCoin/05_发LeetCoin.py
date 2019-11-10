from leezy import Solution, solution


class Node:
    def __init__(self, x):
        self.id = x
        self.boss = self
        self.size = 1
        # type 2 money for this node, this is for followers to query their total coins
        self.team_bouns = 0
        # total coins of this node and its followers
        self.sub_total = 0
        self.sub = []

class Q04(Solution):
    @solution
    def bonus(self, n, leadership, operations):
        # 2492ms  so close in the contest -.-|||
        # on the edge of TLE. sometimes it did TLE
        nodes = [None] + [Node(x) for x in range(1, n+1)]
        for boss, sub in leadership:
            nodes[boss].sub.append(nodes[sub])
            nodes[sub].boss = nodes[boss]
        root = [node for node in nodes[1:] if node.boss == node][0]

        def make_size(node):
            s = 1
            for nxt in node.sub:
                s += make_size(nxt)
            node.size = s
            return node.size
        make_size(root)

        ans = []
        for op in operations:
            p = op[1]
            if op[0] == 1:
                amount = op[2]
                # indivisual bouns, add the amount in current node
                # and report it to all leaders
                node = nodes[p]
                while node.boss != node:
                    node.sub_total += amount
                    node = node.boss
                node.sub_total += amount
            elif op[0] == 2:
                amount = op[2]
                node = nodes[p]
                size = node.size
                # team bouns(type 2), add the amount to team_bouns
                node.team_bouns += amount
                # add the **total** amount and
                # report it to all leaders
                total_bouns = amount * size
                while node.boss != node:
                    node.sub_total += total_bouns
                    node = node.boss
                node.sub_total += total_bouns
            else:
                # when it comes to query, node ask every leader, how much coins are
                # reserved for my team ?
                node = nodes[p]
                coins = node.sub_total
                size = node.size
                while node.boss != node:
                    coins += node.boss.team_bouns * size
                    node = node.boss
                ans.append(coins % 1000000007)
        return ans


def main():
    q = Q04()
    q.add_args(6, leadership=[[1, 2], [1, 6], [2, 3], [2, 5], [1, 4]],
                  operations=[[1, 1, 500], [2, 2, 50], [3, 1], [2, 6, 15], [3, 1]])
    q.run()


if __name__ == "__main__":
    main()
