def max_questions_studied(N, M, times):
    # Sort the list of times required to study each question
    times.sort()

    # Initialize variables
    studied = 0
    total_time = 0

    # Try to study questions in increasing time order
    for time in times:
        if total_time + time <= M:
            total_time += time
            studied += 1
        else:
            break

    return studied


# Input reading
N, M = map(int, input().split())  # Number of questions and time available
times = list(map(int, input().split()))  # List of times required for each question

# Output the maximum number of questions that can be studied
print(max_questions_studied(N, M, times))