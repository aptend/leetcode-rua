from leezy import solution, Solution


class Q1092(Solution):
    @solution
    def shortestCommonSupersequence(self, str1, str2):
        # Memory Limit Exceed
        # 47/47
        m, n = len(str1), len(str2)
        memo = {}

        def match(i, j):
            if i == m:
                return str2[j:]
            if j == n:
                return str1[i:]
            if (i, j) in memo:
                return memo[i, j]
            if str1[i] == str2[j]:
                return str1[i] + match(i+1, j+1)
            candi1 = str2[j] + match(i, j+1)
            candi2 = str1[i] + match(i+1, j)
            opt = candi1 if len(candi1) < len(candi2) else candi2
            memo[i, j] = opt
            return opt
        return match(0, 0)

    @solution
    def shortest_common_superseq_recur(self, str1, str2):
        # 1508ms 5.11%
        m, n = len(str1), len(str2)
        memo, path = {}, {}

        def match(i, j):
            if (i, j) in memo:
                return memo[i, j]
            if i == m:
                opt = n-j
            elif j == n:
                opt = m-i
            elif str1[i] == str2[j]:
                opt = 1 + match(i+1, j+1)
                path[i, j] = (i+1, j+1)
            else:
                candi1 = 1 + match(i, j+1)
                candi2 = 1 + match(i+1, j)
                if candi1 < candi2:
                    opt = candi1
                    path[i, j] = (i, j+1)
                else:
                    opt = candi2
                    path[i, j] = (i+1, j)
            memo[i, j] = opt
            return opt
        match(0, 0)
        ans = ''
        i, j = 0, 0
        while (i, j) in path:
            ni, nj = path[i, j]
            if ni != i:
                ans += str1[i]
            else:
                ans += str2[j]
            i, j = ni, nj
        ans += str1[i:]
        ans += str2[j:]
        return ans

    @solution
    def shortest_common_superseq_iter(self, str1, str2):
        # 764ms 19.81%
        m, n = len(str1), len(str2)
        path = {}
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = i or j
                elif str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    path[i, j] = (i-1, j-1)
                else:
                    candi1 = 1 + dp[i-1][j]
                    candi2 = 1 + dp[i][j-1]
                    if candi1 < candi2:
                        dp[i][j] = candi1
                        path[i, j] = (i-1, j)
                    else:
                        dp[i][j] = candi2
                        path[i, j] = (i, j-1)

        ans = ''
        i, j = m, n
        while (i, j) in path:
            ni, nj = path[i, j]
            if ni != i:
                ans += str1[i-1]
            else:
                ans += str2[j-1]
            i, j = ni, nj
        if i == 0:
            return str2[:j] + ans[::-1]
        else:
            return str1[:i] + ans[::-1]

    @solution
    def shortest_common_superseq_iter2(self, str1, str2):
        # 500ms 61.66%
        m, n = len(str1), len(str2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = i or j
                elif str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])

        ans = ''
        i, j = m, n
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                ans += str1[i-1]
                i -= 1
                j -= 1
            elif dp[i-1][j] < dp[i][j-1]:
                ans += str1[i-1]
                i -= 1
            else:
                ans += str2[j-1]
                j -= 1
        if i == 0:
            return str2[:j] + ans[::-1]
        else:
            return str1[:i] + ans[::-1]


def main():
    q = Q1092()
    q.add_case(q.case('abac', 'cab'))
    q.add_case(q.case('cab', 'abac'))
    q.add_case(q.case('acbbcccaa', 'bbbcaaaaa'))
    q.run()


if __name__ == '__main__':
    main()
