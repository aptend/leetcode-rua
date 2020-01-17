from leezy import Solution, solution


class Q042(Solution):

    @solution
    def trap1(self, height):
        N = len(height)
        if N == 0:
            return 0
        lm = [0] * N
        lm[0] = height[0]
        for i in range(1, N):
            lm[i] = max(lm[i-1], height[i])
        rm = [0] * N
        rm[-1] = height[-1]
        for i in range(N-2, -1, -1):
            rm[i] = max(rm[i+1], height[i])
        ans = 0
        for i in range(N):
            ans += max(0, min(lm[i], rm[i]) - height[i])
        return ans

    @solution
    def trap2(self, height):
        N = len(height)
        if N == 0:
            return 0
        ans = 0
        i, j = 1, N-2
        lm, rm = height[0], height[-1]
        while i <= j:
            if lm < rm:
                ans += max(0, lm - height[i])
                lm = max(lm, height[i])
                i += 1
            else:
                ans += max(0, rm - height[j])
                rm = max(rm, height[j])
                j -= 1
        return ans

    @solution
    def trap3(self, height):
        ans = 0
        stack = [0]
        for i, h in enumerate(height[1:], 1):
            # append same height, or it would be wrong
            # when it becomes the left boundary of a pool
            if h <= height[stack[-1]]:
                stack.append(i)
                continue
            while h > height[stack[-1]]:
                bottom = height[stack.pop()]
                if not stack:
                    break
                up = min(height[stack[-1]], h)
                ans += (up - bottom) * (i - stack[-1] - 1)
            stack.append(i)
        return ans


def main():
    q = Q042()
    q.add_case(q.case([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]).assert_equal(6))
    q.add_case(q.case([5, 2, 1, 2, 1, 5]).assert_equal(14))
    q.add_case(q.case([6, 10, 21, 67, 8, 55, 62, 13,
                       51, 67, 63, 68]).assert_equal(150))
    q.run()


if __name__ == "__main__":
    main()
