coins = [1,2,5]
x = 11
def coin_change(coins,x):
    dp = [float('inf')] *(x +1)
    dp[0] =0
    for coin in coins:
        for i in range(coin,x+1):
            dp[i] =min(dp[i],dp[i -coin] + 1)
    return dp[x] if  dp[x] != float('inf') else -1
print(coin_change(coins,x))