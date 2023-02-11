class Solution:
    def minFallingPathSum(self, matrix):


        for i in range(1, len(matrix)):
            for j in range(len(matrix[i])):
                left_side = max(j - 1, 0)
                right_side = min(j + 1, len(matrix[i]) - 1)
                curr_scope = matrix[i - 1][left_side:right_side + 1]
                matrix[i][j] += min(curr_scope)

        return min(matrix[-1])

ans = Solution()
matrix = [[2,1,3],[6,5,4],[7,8,9]]
print(ans.minFallingPathSum(matrix))

