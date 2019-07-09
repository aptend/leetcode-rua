from leeyzer import Solution, solution


class Q011(Solution):
    @solution
    def maxArea(self, height):
        l, r = 0, len(height)-1
        max_area = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_area



def main():
    q = Q011()
    q.add_args([1, 1])
    q.add_args([1, 8, 6, 2, 5, 4, 8, 3, 7])
    q.run()


if __name__ == "__main__":
    main()
