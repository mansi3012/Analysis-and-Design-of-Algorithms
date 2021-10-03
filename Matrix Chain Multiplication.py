# Matrix Chain Multiplication using Python

def MatChainMul(a, n):
    dp = [[0 for i in range(n)] for j in range(n)]
    
    for i in range(1, n):
        dp[i][i] = 0

    for L in range(2, n):
        
        for i in range(1, n - L + 1):
            
            j = i + L - 1
            dp[i][j] = 10 ** 10
            
            for k in range(i, j):
                
                q = dp[i][k] + dp[k + 1][j] + a[i - 1] * a[k] * a[j]
                
                if q < dp[i][j]:
                    dp[i][j] = q

    return dp[1][n - 1]

a = [10,30,5,60]
size = len(a)

print("The Minimum cost is: " + str(MatChainMul(a, size)))
