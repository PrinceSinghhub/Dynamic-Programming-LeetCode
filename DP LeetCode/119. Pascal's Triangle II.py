class Solution:
    def getRow(self, rowIndex):

        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        pascal = [[1]]

        for i in range(1, rowIndex + 1):
            row = [1]
            for j in range(1, i):
                row.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
            row.append(1)
            pascal.append(row)

        return pascal[rowIndex]

ans = Solution()
n = 3
print(ans.getRow(n))