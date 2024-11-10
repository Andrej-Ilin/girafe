"""https://miniapps.ai/chatgpt/c/cb41d5a6-3d18-4532-99ec-a537dad459be"""


def knapsack(capacity, weights, costs):
    N = len(weights)

    # Create a DP array
    dp = [[0] * (capacity + 1) for _ in range(N + 1)]

    # Build the DP table
    for i in range(1, N + 1):
        for j in range(capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], costs[i - 1] + dp[i - 1][j - weights[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]

    # Maximum profit
    max_profit = dp[N][capacity]

    # Determine which items to include
    selected_items = []
    w = capacity
    for i in range(N, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # This means item i was included
            selected_items.append(i)  # Store the index (1-indexed)
            w -= weights[i - 1]

    selected_items.reverse()  # To maintain the order of indices

    # Print the results
    print(max_profit)
    print(len(selected_items))
    if selected_items:
        print(" ".join(map(str, selected_items)))
    else:
        print()


# Input reading
capacity, N = map(int, input().strip().split())
weights = list(map(int, input().strip().split()))
costs = list(map(int, input().strip().split()))

# Call the knapsack function
knapsack(capacity, weights, costs)