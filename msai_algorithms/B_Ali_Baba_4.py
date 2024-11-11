"https://contest.yandex.ru/contest/70070/problems/B/"


def can_partition(costs):
    total_sum = sum(costs)

    # If the total sum is odd, we cannot partition it into two equal subsets
    if total_sum % 2 != 0:
        return "NO"

    target = total_sum // 2
    n = len(costs)

    # DP array to track achievable sums
    dp = [False] * (target + 1)
    dp[0] = True  # Sum of 0 is always achievable

    # Fill the DP array
    for cost in costs:
        for j in range(target, cost - 1, -1):  # Update backwards
            dp[j] = dp[j] or dp[j - cost]

    return "YES" if dp[target] else "NO"


# Input reading
n = int(input().strip())
costs = list(map(int, input().strip().split()))

# Check if partition is possible and print the result
result = can_partition(costs)
print(result)
