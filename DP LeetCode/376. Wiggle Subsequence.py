class Solution:
    def wiggleMaxLength(self, nums):

        L = len(nums)
        dp = [(0, None)] * L
        for i in range(1, L):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff != 0 and ((diff > 0) != dp[j][1]):
                    if 1 + dp[j][0] > dp[i][0]:
                        dp[i] = (1 + dp[j][0], diff > 0)
        return max(dp, key=lambda x: x[0])[0] + 1

nums = [1,7,4,9,2,5]
ans = Solution()
print(ans.wiggleMaxLength(nums))