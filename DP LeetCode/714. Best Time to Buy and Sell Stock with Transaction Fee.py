class Solution:
    def maxProfit(self, prices,fee):
        bsp = -prices[0]
        ssp = 0

        for i in range(1, len(prices)):
            nbsp = max(bsp, ssp - prices[i])
            nssp = max(ssp, prices[i] + bsp - fee)

            bsp = nbsp
            ssp = nssp

        return ssp
ans = Solution()
prices = [1,3,2,8,4,9]
fee = 2
print(ans.maxProfit(prices,fee))
