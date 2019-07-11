from leeyzer import Solution, solution


class Q084(Solution):
    @solution
    def largestRectangleArea(self, heights):
        # 一开始的分类不对，这样代表以当前条柱开始的长方形
        # 所以[2, 1, 2]这样的的图，最长的不是以1开始的长方形
        # 而是以1为高的长方形
        # 所以记录了一个width，当前条左边有多少个比它大的
        stack = [0]
        left_higher = [0] * (len(heights)+1)
        max_area = 0
        heights = heights + [0]
        for i, h in enumerate(heights[1:], 1):
            while stack and heights[stack[-1]] > h:
                j = stack.pop()
                width = i - j + left_higher[j]
                area = heights[j] * width
                left_higher[i] = width
                max_area = max(max_area, area)
            stack.append(i)
        return max_area

    @solution
    def largest_area(self, heights):
        # 实际上width等于栈中左边条的索引值，因为每次循环都把左边比它大的pop掉，不用再重复记录
        heights = heights + [0]
        stack = [-1] # 利用python的-1索引
        max_area = 0
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                j = stack.pop()
                width = i - stack[-1] - 1
                area = heights[j] * width
                max_area = max(max_area, area)
            stack.append(i)
        return max_area



def main():
    q = Q084()
    q.add_args([1])
    q.add_args([2, 1, 2]) # 3
    q.add_args([3,6,5,7,4,8,1,0]) # 20
    q.add_args([2, 1, 5, 6, 2, 3]) # 10
    q.add_args([2, 7, 1, 8, 8, 3, 11, 12, 13, 3]) # 33
    q.run()


if __name__ == "__main__":
    main()
