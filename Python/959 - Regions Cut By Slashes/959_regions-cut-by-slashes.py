from leeyzer import Solution, solution


class UF:
    def __init__(self, size):
        self.parents = list(range(size))
        self.ranks = [0] * size
        self.count = size
    
    def find(self, p):
        if p != self.parents[p]:
            self.parents[p] = self.find(self.parents[p])
        return self.parents[p]

    def insert_slot(self):
        id_ = len(self.parents)
        self.parents.append(id_)
        self.ranks.append(0)
        self.count += 1
        return id_

    def union(self, p, q):
        rp = self.find(p)
        rq = self.find(q)
        if rp == rq:
            return
        if self.ranks[rp] > self.ranks[rq]:
            self.parents[rq] = rp
        elif self.ranks[rp] < self.ranks[rq]:
            self.parents[rp] = rq
        else:
            self.parents[rp] = rq
            self.ranks[rq] += 1
        self.count -= 1



class Q959(Solution):
    @solution
    def regionsBySlashes(self, grid):
        # 112ms 81.13%
        def query_low_id(i, j):
            if grid[i][j] == ' ' or grid[i][j] == '/':
                return (i * N + j) * 2 + 1 # id2 can be unioned with lower cell
            else:
                return (i * N + j) * 2 # id1 can be unioned with lower cell

        # every slash divides a cell into 2 parts, 
        # id1 means the left part and id2 means the right part
        # blank space can be seen as /, but the divided parts are union naturally
        N = len(grid)
        uf = UF(N*N*2)
        for i in range(N):
            for j in range(N):
                ch = grid[i][j]
                id1 = (i * N + j) * 2
                id2 = id1+1
                if ch == ' ':
                    uf.union(id1, id2)
                if j > 0:  # union left neighbor
                    uf.union(id1, id1-1)
                if i > 0:  # union up neighbor
                    if ch == ' ' or ch == '/':
                        uf.union(id1, query_low_id(i-1, j))
                    else:
                        uf.union(id2, query_low_id(i-1, j))
        return uf.count


def main():
    q = Q959()
    q.add_args([" /", "/ "])  # 2
    q.add_args(["\\/", "/\\"])  # 4
    q.add_args([" /", "  "])  # 1
    q.add_args(["/\\", "\\/"])  # 5
    q.add_args(["//", " /"])  # 3
    q.run()


if __name__ == "__main__":
    main()
