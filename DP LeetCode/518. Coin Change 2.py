class Solution:
    def change(self, amount, coins):

        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:

            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[-1]

ans = Solution()
amount = 5
coins = [1,2,5]
print(ans.change(amount,coins))