def count_representable_numbers(n: int, arr: list[int]) -> int:
    # Set to store all possible sums of two elements
    sums = set()
    for i in range(n):
        for j in range(i + 1, n):
            sums.add(arr[i] + arr[j])

    # Count how many numbers in the array are in the set of sums
    count = 0
    for num in arr:
        if num in sums:
            count += 1
    return count


# Example usage
if __name__ == "__main__":
    # Input reading
    n = int(input())
    arr = list(map(int, input().split()))

    # Output the result
    print(count_representable_numbers(n, arr))