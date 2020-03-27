from leezy import Solution, solution


class Q093(Solution):
    @solution
    def restoreIpAddresses(self, s):
        # 24ms 66.06%
        formed, total = [], []
        self.dfs(s, 4, 0, formed, total)
        return total

    def dfs(self, s, n, start, formed, total):
        if n == 0:
            if start == len(s):
                total.append('.'.join(formed))
            return
        for i in range(start, min(len(s), start+3)):
            option = s[start:i+1]
            if len(option) > 1 and option.startswith('0'):
                break
            if int(option) > 255:
                break
            formed.append(option)
            self.dfs(s, n-1, i+1, formed, total)
            formed.pop()


def main():
    q = Q093()
    q.add_case(q.case('25525511135')
                .assert_equal(["255.255.11.135", "255.255.111.35"]))
    q.add_case(q.case('11111')
                .assert_equal(["1.1.1.11", "1.1.11.1", "1.11.1.1", "11.1.1.1"]))
    q.add_case(q.case('010010').assert_equal(["0.10.0.10", "0.100.1.0"]))
    q.run()


if __name__ == "__main__":
    main()
