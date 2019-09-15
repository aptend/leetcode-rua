from leeyzer import Solution, solution


class Q084(Solution):
    """Ref to 901. Online Stock span
    """
    @solution
    def largestRectangleArea(self, heights):
        # TLE 
        # tests passed: 94/96
        # the basic idea is to try every max rectangle having height[i]
        # what we need to kown is,
        #  how many continuous bars are `ge` than height[i] on its left
        #  how many continuous bars are `ge` than height[i] on its right
        ans = 0
        for i, h in enumerate(heights):
            l_cnt = r_cnt = 0
            for j in range(i-1, -1, -1):
                if heights[j] >= h:
                    l_cnt += 1
                else:
                    break
            
            for j in range(i+1, len(heights)):
                if heights[j] >= h:
                    r_cnt += 1
                else:
                    break
            ans = max(ans, h * (1 + l_cnt + r_cnt))
        return ans

    @solution
    def largest_rect_area(self, heights):
        # 108ms 14.33%
        # let's use `jump list` to compute the info that we need in advance
        N = len(heights)
        # left[i] means how many bars `ge` than heights[i] on its left
        # we can reuse the infomation of left[]
        left = [0] * N
        for i in range(N):
            j = i
            while j >= 0 and heights[j] >= heights[i]:
                j = j - left[j] - 1
            left[i] = i - j - 1
        right = [0] * N
        for i in range(N-1, -1, -1):
            j = i
            while j < N and heights[j] >= heights[i]:
                j = j + right[j] + 1
            right[i] = j - i - 1
        ans = 0
        for i, h in enumerate(heights):
            ans = max(ans, h * (1 + left[i] + right[i]))
        return ans

    @solution
    def largest_rect_area_stack(self, heights):
        # 108ms
        # we can also use monotonic stack to find `left` and `right`
        N = len(heights)
        stack = []
        left = [0] * N
        for i in range(N):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            # when while loop exited, we know that heights[stack[-1]] < heights[i]
            # which is left boundary, we can calculate how many hihger bars on the left
            left[i] = i - stack[-1] - 1 if stack else i
            stack.append(i)
        stack = []
        right = [0] * N
        for i in range(N-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] - i - 1 if stack else N-1-i
            stack.append(i)
        ans = 0
        for i, h in enumerate(heights):
            ans = max(ans, h * (1 + left[i] + right[i]))
        return ans


    @solution
    def largest_area(self, heights):
        # 88ms 77.03%
        heights = heights + [0] # append a 0 height, make sure to pop every bar
        stack = [-1] # 
        max_area = 0
        for i, h in enumerate(heights):
            while heights[stack[-1]] > h:
                # actually, when we encounter a smaller (not including equal) bar,
                # this is a right boundry
                # every higher bar 'h_x' in the stack could be popped and 
                # calculated the max rect with height 'h_x'
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
    q.add_args([3, 6, 5, 7, 4, 8, 1, 0]) # 20
    q.add_args([2, 1, 5, 6, 2, 3]) # 10
    q.add_args([2, 7, 1, 8, 8, 3, 11, 12, 13, 3]) # 33
    q.run()


if __name__ == "__main__":
    main()
