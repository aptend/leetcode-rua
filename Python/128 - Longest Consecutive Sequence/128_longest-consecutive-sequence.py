from leezy import solution, Solution


class Q128(Solution):
    @solution
    def longestConsecutive(self, nums):
        # 60ms 81.38%
        stat = {}
        ans = 0
        for x in nums:
            if x in stat:
                continue
            length = 1
            if x - 1 in stat:
                # can be placed in a right end
                length += stat[x-1]
            if x + 1 in stat:
                # can be placed in a left end
                length += stat[x+1]
            if x - 1 in stat:
                stat[x - stat[x-1]] = length
            if x + 1 in stat:
                stat[x + stat[x+1]] = length
            ans = max(ans, length)
            stat[x] = length
        return ans



def main():
    q = Q128()
    q.add_case(q.case([100, 4, 200, 1, 3, 2]).assert_equal(4))
    q.add_case(q.case([100, -1, 4, 200, 1, 3, 2, 0]).assert_equal(6))
    q.run()

if __name__ == '__main__':
    main()
