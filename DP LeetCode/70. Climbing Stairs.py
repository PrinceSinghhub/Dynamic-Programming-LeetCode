# another approch Space Optimization
class Solution1:
    def climbStairs(self, n):

        # todo using Spacae OPtimizarion

        if n < 2:
            return n

        first = 1
        second = 1

        for i in range(2, n + 1):
            ans = first + second
            first = second
            second = ans
        return second


from numpy import *
class Solution:
    def climbStairs(self, n):

        if n<2:
            return n

        arr = zeros((n),int)
        arr[0] = 1
        arr[1] = 2

        for i in range(2,len(arr)):
            first = arr[i-1]
            second = arr[i-2]

            arr[i] = first+second
        return arr[n-1]
ans = Solution()
print(ans.climbStairs(11))

