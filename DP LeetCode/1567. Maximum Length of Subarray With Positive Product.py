class Solution:
    def getMaxLen(self, nums):

        positive = 0
        negative = 0
        result = 0

        for n in nums:
            if n == 0:
                positive = 0
                negative = 0
            elif n > 0:
                positive += 1
                if negative == 0:
                    negative = 0
                else:
                    negative+=1
            else:
                temp = positive
                positive = 0 if negative == 0 else negative+1
                negative = temp + 1
            result = max(result, positive)
        return result

ans = Solution()
nums = [1,-2,-3,4]
print(ans.getMaxLen(nums))
