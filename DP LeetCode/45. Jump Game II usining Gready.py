class Solution:
    def jump(self, nums):

        currReach = 0
        currMax = 0
        Jumps = 0

        for i in range(len(nums)-1):

            if i+nums[i]>currMax:
                currMax = i+nums[i]

            if i == currReach:
                Jumps+=1
                currReach = currMax
        return Jumps

ans = Solution()
nums = [2,3,1,1,4]
print(ans.jump(nums))
