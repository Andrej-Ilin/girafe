def mars_cucumbers(n: int, rains: list[tuple[int, int]], queries: list[tuple[int, int]]) -> list[int]:
    """
    Calculate the total water collected in given ranges for the cucumbers on Mars.

    Args:
        n (int): Number of pots.
        rains (list[tuple[int, int]]): List of rain ranges [l, r).
        queries (list[tuple[int, int]]): List of query ranges [ql, qr).

    Returns:
        list[int]: List of query results.
    """
    # Step 1: Initialize the difference array
    diff = [0] * (n + 1)
    for l, r in rains:
        diff[l] += 1
        if r < n:
            diff[r] -= 1

    # Step 2: Compute the total water in each pot using prefix sums
    water = [0] * n
    water[0] = diff[0]
    for i in range(1, n):
        water[i] = water[i - 1] + diff[i]

    # Step 3: Compute the prefix sum for water to allow range sum queries
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + water[i]

    # Step 4: Process the queries
    results = []
    for ql, qr in queries:
        results.append(prefix_sum[qr] - prefix_sum[ql])

    return results


# Example usage
if __name__ == "__main__":
    # Read inputs
    n, m, k = map(int, input().split())
    rains = [tuple(map(int, input().split())) for _ in range(m)]
    queries = [tuple(map(int, input().split())) for _ in range(k)]

    # Get results and print them
    results = mars_cucumbers(n, rains, queries)
    print("\n".join(map(str, results)))