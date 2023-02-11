class Solution:
    def matrixBlockSum(self, mat, k):

        M, N = len(mat), len(mat[0])
        dp = [[0 for _ in range(N)] for _ in range(M)]

        for i in range(M):
            for j in range(N):
                MIN = max(0, i - k)
                MAX = min(i + k, M - 1)
                if i == 0:
                    for k in range(MIN, MAX + 1):
                        dp[i][j] += mat[k][j]
                else:
                    SUB = 0 if MIN == 0 else mat[MIN - 1][j]
                    ADD = 0 if i + k >= M else mat[MAX][j]
                    dp[i][j] += dp[i - 1][j] - SUB + ADD

        res = [[0 for _ in range(N)] for _ in range(M)]
        for i in range(M):
            for j in range(N):
                MIN = max(0, j - k)
                MAX = min(j + k, N - 1)
                if j == 0:
                    for k in range(MIN, MAX + 1):
                        res[i][j] += dp[i][k]
                else:
                    SUB = 0 if MIN == 0 else dp[i][MIN - 1]
                    ADD = 0 if j + k >= N else dp[i][MAX]
                    res[i][j] += res[i][j - 1] - SUB + ADD

        return res


ans = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(ans.matrixBlockSum(mat,k))