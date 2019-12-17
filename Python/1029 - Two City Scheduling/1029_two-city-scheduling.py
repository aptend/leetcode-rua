from leezy import solution, Solution


class Q1029(Solution):
    @solution
    def two_city_cost(self, costs):
        # 40ms 79.25%
        # all people go to A
        total_cost = sum(c[0] for c in costs)

        N = len(costs) // 2
        # change N persons to B
        for delta in sorted(c[1]-c[0] for c in costs)[:N]:
            total_cost += delta
        return total_cost

    @solution
    def twoCitySchedCost(self, costs):
        # 40ms
        a_cnt = 0
        b_cnt = 0
        N = len(costs) // 2
        total_cost = 0
        costs = sorted(costs, key=lambda c: abs(c[0] - c[1]), reverse=True)
        for to_a, to_b in costs:
            if a_cnt == N:
                b_cnt += 1
                total_cost += to_b
            elif b_cnt == N:
                a_cnt += 1
                total_cost += to_a
            elif to_a < to_b:
                a_cnt += 1
                total_cost += to_a
            elif to_a > to_b:
                b_cnt += 1
                total_cost += to_b
            else:
                if a_cnt < b_cnt:
                    a_cnt += 1
                else:
                    b_cnt += 1
                total_cost += to_a
        return total_cost


def main():
    q = Q1029()
    q.add_case(
        q.case([[10, 20], [30, 200], [400, 50], [30, 20]]).assert_equal(110))
    q.run()


if __name__ == '__main__':
    main()
