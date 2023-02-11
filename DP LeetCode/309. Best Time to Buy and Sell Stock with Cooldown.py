class Solution:
    def maxProfit(self, prices):
        size = len(prices)
        if size < 2: return 0
        hold, unhold, cooldown = float('-inf'),0,0
        print(cooldown)
        for price in prices:
            hold=max(hold,cooldown-price)
            cooldown = max(cooldown, unhold)
            unhold=max(unhold,hold+price)
        return unhold

ans = Solution()
prices = [1,2,3,0,2]
print(ans.maxProfit(prices))