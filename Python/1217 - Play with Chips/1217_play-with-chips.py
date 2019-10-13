from leeyzer import Solution, solution


class Q1217(Solution):
    @solution
    def minCostToMoveChips(self, chips):
        odd = 0
        even = 0
        for x in chips:
            if x % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(even, odd)



def main():
    q = Q1217()
    q.add_args([1, 2, 3])
    q.run()


if __name__ == "__main__":
    main()
