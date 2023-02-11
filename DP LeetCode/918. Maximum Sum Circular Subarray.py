class Solution:
    def maxSubarraySumCircular(self, nums):

        # apply before change the element sign
        ans = self.kandals(nums)

        circularSubarr = 0
        for i in nums:
            circularSubarr+=i

        # change the sign of all element
        for i in range(len(nums)):
            nums[i] = nums[i]*-1

        # apply after change the element sign
        circularSubarr_ans = self.kandals(nums)

        if circularSubarr+circularSubarr_ans == 0:
            return ans
        return max(ans,circularSubarr_ans+circularSubarr)



    def kandals(self, nums):

        boolen = True
        for i in nums:
            if i < 0:
                pass
            else:
                boolen = False
                break
        if boolen == True:
            return max(nums)

        max_sum = 0
        cur_sum = 0

        for i in range(len(nums)):
            cur_sum = cur_sum + nums[i]
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return max_sum

ans = Solution()
nums = [1,-2,3,-2]
print(ans.maxSubarraySumCircular(nums))