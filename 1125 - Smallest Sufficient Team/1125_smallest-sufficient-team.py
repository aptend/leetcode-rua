from leeyzer import Solution, solution


class Q1125(Solution):
    @solution
    def smallestSufficientTeam(self, req_skills, people):
        # 856ms 15.28%
        # it not the fastest, but it has better affinity with normal knapsack problem
        N = len(req_skills)
        all_skl = (1 << N) - 1
        skl_map = []
        for p in people:
            state = 0
            for skl in p:
                state |= 1 << req_skills.index(skl)
            skl_map.append(state)
        
        MAX = float('inf')
        dp = [MAX] * (1 << N)
        dp[0] = 0
        trace = [None] * (1 << N)
        for i, p_skl in enumerate(skl_map):
            for team_skl in range(all_skl, -1, -1):
                # push is better than pull here
                if dp[team_skl] + 1 < dp[team_skl | p_skl]:
                    dp[team_skl | p_skl] = dp[team_skl] + 1
                    trace[team_skl | p_skl] = (team_skl, i)

        ans = []
        skl = all_skl
        while skl:
            ans.append(trace[skl][1])
            skl = trace[skl][0]
        return ans

    @solution
    def smallest_sufficient_team(self, req_skills, people):
        # 196ms 66.67%
        # this is another way to express the essence of dp, the subproblem
        N = len(req_skills)
        dp = {0: []}
        for i, p in enumerate(people):
            his_skill = 0
            for skill in p:
                his_skill |= 1 << req_skills.index(skill)
            for skill_set, need in list(dp.items()):
                with_him = skill_set | his_skill
                if with_him == skill_set:
                    continue
                if with_him not in dp or len(dp[with_him]) > len(need) + 1:
                    dp[with_him] = need + [i]
        return dp[(1 << N) - 1]



def main():
    q = Q1125()
    q.add_args(['java', 'nodejs', 'reactjs'], [['java'], ['nodejs'], ['nodejs', 'reactjs']])
    q.add_args(["algorithms", "math", "java", "reactjs", "csharp", "aws"],
               [["algorithms", "math", "java"],
                ["algorithms", "math", "reactjs"],
                ["java", "csharp", "aws"],
                ["reactjs", "csharp"],
                ["csharp", "math"],
                ["aws", "java"]])
    q.run()


if __name__ == "__main__":
    main()
