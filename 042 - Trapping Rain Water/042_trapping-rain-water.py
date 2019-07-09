from leeyzer import Solution, solution


class Q042(Solution):
    @solution
    def trap(self, height):
        volume = 0
        stack = [0]
        for i, h in enumerate(height[1:], 1):
            if h <= height[stack[-1]]:  # append same height, or it would be wrong 
                                   # when it becomes the left boundary of a pool
                stack.append(i)
                continue
            while h > height[stack[-1]]:
                bottom = height[stack.pop()]
                if not stack:
                    break
                up = min(height[stack[-1]], h)
                volume += (up - bottom) * (i - stack[-1] - 1)
            stack.append(i)
        return volume


def main():
    q = Q042()
    q.add_args([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])  # 6
    q.add_args([5, 2, 1, 2, 1, 5])  # 14
    q.add_args([6, 10, 21, 67, 8, 55, 62, 13, 51, 67, 63, 68])  # 150
    q.run()


if __name__ == "__main__":
    main()
