from leeyzer import Solution, solution


class Q696(Solution):
    @solution
    def countBinarySubstrings(self, s):
        cnt0 = 0
        cnt1 = 0
        prev = -1
        ans = 0
        for x in s:
            if x != prev:
                ans += min(cnt0, cnt1)
                if x == '1':
                    cnt1 = 0
                else:
                    cnt0 = 0
            if x == '1':
                cnt1 += 1
            else:
                cnt0 += 1
            prev = x
        ans += min(cnt0, cnt1)
        return ans


def main():
    q = Q696()
    q.add_args('00110')
    q.add_args('10101')
    q.add_args('00110011')
    q.run()


if __name__ == "__main__":
    main()
