from leeyzer import Solution, solution

from functools import reduce
class Q399(Solution):
    @solution
    def calcEquation(self, equations, values, queries):
        """
        本质就是图的联通性
        """
        mapping = {}
        for (x, y), r in zip(equations, values):
            if x not in mapping:
                mapping[x] = set()
            if y not in mapping:
                mapping[y] = set()
            mapping[x].add((y, r))
            mapping[y].add((x, 1/r))

        def path_between(qx, qy, seen, path_vals):
            seen.add(qx)
            if qx == qy:
                return True
            for step in mapping[qx]:
                if step[0] in seen:
                    continue
                if path_between(step[0], qy, seen, path_vals):
                    path_vals.append(step[1])
                    return True
            return False

        results = []
        for qx, qy in queries:
            if qx not in mapping or qy not in mapping:
                results.append(-1.0)
            elif qx == qy:
                results.append(1.0)
            else:
                seen = set()
                vals = []
                path_between(qx, qy, seen, vals)
                if vals:
                    results.append(reduce(lambda x, y: x*y, vals, 1.0))
                else:
                    results.append(-1.0)                
        return results



def main():
    q = Q399()
    q.add_args([['a', 'b'], ['b', 'c'], ['m', 'n']], [2.0, 3.0, 4.0], [
               ['a', 'c'], ['b', 'a'], ['a', 'm'], ['a', 'a'], ['x', 'x']])
    q.run()


if __name__ == "__main__":
    main()
