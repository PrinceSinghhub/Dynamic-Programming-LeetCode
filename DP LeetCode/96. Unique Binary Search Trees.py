class Solution:
    def numTrees(self, n):

        BTree = [1, 1]

        for j in range(2, n + 1):
            sum = 0
            for i in range(1, j + 1):
                fi = BTree[i - 1] * BTree[j - i]
                sum += fi
            BTree.append(sum)

        return BTree[n]

ans = Solution()
n = 5
print(ans.numTrees(n))