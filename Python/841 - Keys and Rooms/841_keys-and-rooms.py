from leeyzer import Solution, solution


class Q841(Solution):
    @solution
    def canVisitAllRooms(self, rooms):
        # 40ms 98.05ms / 52ms
        def dfs(i):
            visited[i] = True
            for nxt in rooms[i]:
                if not visited[nxt]:
                    dfs(nxt)

        visited = [False] * len(rooms)
        dfs(0)
        return all(visited)


def main():
    q = Q841()
    q.add_args([[1], [2], [3], []])
    q.add_args([[1, 3], [3, 0, 1], [2], []])
    q.run()


if __name__ == "__main__":
    main()
