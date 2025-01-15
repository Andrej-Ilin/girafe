def partial_sum(n, a):
    list_n = []
    # print(n)
    if a == 1:
        return (n * (n + 1)) // 2
    else:
        for i in range(1, n + 1):
            # print(i)
            count = i * a**i
            # print(count)
            list_n.append(count)
            sum_n_a = sum(list_n)
        return sum_n_a


# Example usage:
if __name__ == "__main__":
    # Example inputs
    n, a = map(int, input().split())
    print(partial_sum(n, a))