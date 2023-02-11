class Solution:
    def maximalSquare(self, matrix):
        if len(matrix) == 0:
            return 0

        n, m = len(matrix), len(matrix[0])

        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

        max_square = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_square = max(max_square, dp[i][j])
        return max_square ** 2

ans = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(ans.maximalSquare(matrix))