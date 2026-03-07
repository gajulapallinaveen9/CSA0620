def min_production_time(station_times, transfer):
    
    lines = len(station_times)
    stations = len(station_times[0])

    dp = [[float('inf')] * lines for _ in range(stations)]

    # First station
    for j in range(lines):
        dp[0][j] = station_times[j][0]

    # Compute DP
    for i in range(1, stations):
        for j in range(lines):
            for k in range(lines):
                time = dp[i-1][k] + transfer[k][j] + station_times[j][i]
                dp[i][j] = min(dp[i][j], time)

    return min(dp[stations-1])


station_times = [
    [5, 9, 3],   # Line 1
    [6, 8, 4],   # Line 2
    [7, 6, 5]    # Line 3
]

transfer = [
    [0, 2, 3],
    [2, 0, 4],
    [3, 4, 0]
]

result = min_production_time(station_times, transfer)

print("Minimum Production Time:", result)
