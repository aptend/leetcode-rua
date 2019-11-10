from leezy import Solution, solution


class Q1213(Solution):
    @solution
    def arraysIntersection(self, arr1, arr2, arr3):
        return list(sorted(set(arr1) & set(arr2) & set(arr3)))

    @solution
    def array_intersection(self, arr1, arr2, arr3):
        i1 = i2 = i3 = 0
        a1, a2, a3 = arr1, arr2, arr3
        ans = []
        while i1 < len(a1) and i2 < len(a2) and i3 < len(a3):
            v1, v2, v3 = a1[i1], a2[i2], a3[i3]
            if v1 == v2 == v3:
                ans.append(v1)
                i1 += 1
                i2 += 1
                i3 += 1
                continue
            m = max(v1, v2, v3)
            if v1 < m:
                i1 += 1
            if v2 < m:
                i2 += 1
            if v3 < m:
                i3 += 1
        return ans


def main():
    q = Q1213()
    q.add_args([1, 2, 3, 4, 5], [1, 2, 5, 7, 9], [1, 3, 4, 5, 8])
    q.run()


if __name__ == "__main__":
    main()
