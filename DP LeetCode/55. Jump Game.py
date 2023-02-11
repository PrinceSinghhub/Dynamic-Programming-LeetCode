class Solution:
    def canJump(self, nums):


        if len(nums)<2:
            return True
        MaxJuump = 0+nums[0]
        index = 1

        while MaxJuump>=index:

            if MaxJuump >= len(nums)-1:
                return True

            MaxJuump = max(nums[index]+index,MaxJuump)
            index+=1
        return False




ans = Solution()
nums = [1,0,1,0]
print(ans.canJump(nums))
