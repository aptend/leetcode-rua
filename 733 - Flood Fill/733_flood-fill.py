from leeyzer import Solution, solution


class Q733(Solution):
    @solution
    def floodFill(self, image, sr, sc, newColor):
        # 56ms 92.53% / 60ms
        old_color = image[sr][sc]
        if not image or newColor == old_color:
            return image

        m, n = len(image), len(image[0])

        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n):
                return
            if image[i][j] != old_color:
                return
            image[i][j] = newColor
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        dfs(sr, sc)
        return image


def main():
    q = Q733()
    q.add_args([[1, 1, 1],
                [1, 1, 0],
                [1, 0, 1]], 1, 1, 2)
    q.add_args([[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]], 0, 0, 2)
    q.run()


if __name__ == "__main__":
    main()
