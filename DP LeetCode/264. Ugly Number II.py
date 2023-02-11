class Solution:
    def nthUglyNumber(self, n):

        DP = [0] * n
        A = B = C = 0
        DP[0] = 1
        for i in range(1, n):
            DP[i] = min(DP[A] * 2, DP[B] * 3, DP[C] * 5)
            if (DP[i] == DP[A] * 2):
                A += 1
            if (DP[i] == DP[B] * 3):
                B += 1
            if (DP[i] == DP[C] * 5):
                C += 1
        return DP[n - 1]

ans = Solution()
n = 10
print(ans.nthUglyNumber(n))
