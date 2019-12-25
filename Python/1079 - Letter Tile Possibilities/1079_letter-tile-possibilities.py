from leezy import solution, Solution


class Q1079(Solution):
    @solution
    def numTilePossibilities(self, tiles):
        # 100ms 53.85%
        tiles = sorted(tiles)

        def dfs(used, formed):
            if formed:
                yield formed
            prev = ''
            for i in range(len(tiles)):
                if used[i]:
                    continue
                if i == 0 or tiles[i] != prev:
                    used[i] = True
                    prev = tiles[i]
                    yield from dfs(used, formed + tiles[i])
                    used[i] = False

        used = [False] * len(tiles)
        return len(list(dfs(used, '')))


def main():
    q = Q1079()
    q.add_case(q.case('AAB'))
    q.run()


if __name__ == '__main__':
    main()
