from leeyzer import Solution, solution


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
                continue
            if int(option) > 255:
                continue
            formed.append(option)
            self.dfs(s, n-1, i+1, formed, total)
            formed.pop()

def main():
    q = Q093()
    q.add_args('25525511135')
    q.add_args('11111')
    q.add_args('010010')
    q.run()


if __name__ == "__main__":
    main()
