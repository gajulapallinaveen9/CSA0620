import bisect

def jobScheduling(startTime, endTime, profit):
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
    dp = [(0,0)]  # (endTime, maxProfit)

    for s,e,p in jobs:
        i = bisect.bisect(dp, (s, float('inf'))) - 1
        curr_profit = dp[i][1] + p
        if curr_profit > dp[-1][1]:
            dp.append((e, curr_profit))

    return dp[-1][1]


# Test
print(jobScheduling([1,2,3,3],[3,4,5,6],[50,10,40,70]))  # Output: 120
