class Solution:
    def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if 0 < n <= 2:
#             return 1

#         dp = [0 for _ in range(n+1)]
#         dp[0] = 0
#         dp[1] = 1

#         for i in range(2, n+1):
#             dp[i] = dp[i-1] + dp[i-2]
        
#         return dp[-1]


        dp = [-1 for _ in range(n+1)]
        
        def fibo(n):
            if n == 0:
                dp[0] = 0
                return 0
            elif n == 1:
                dp[1] = 1
                return 1
            elif n == 2:
                dp[2] = 1
                return 1

            if dp[n] == -1:
                dp[n] = fibo(n-1) + fibo(n-2)
            
            return dp[n]
        
        fibo(n)
        return dp[-1]