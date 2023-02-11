class Solution:
    def canJump(self, nums):
        length = len(nums)
        dp = [0] * length

        dp[0] = nums[0]

        for i in range(1, length - 1):

            if dp[i - 1] < i:
                return False

            dp[i] = max(i + nums[i], dp[i - 1])

            if dp[i] >= length - 1:
                return True

        print(dp)

        return dp[length - 2] >= length - 1

ans = Solution()
nums = [1,1,1,0]
print(ans.canJump(nums))
