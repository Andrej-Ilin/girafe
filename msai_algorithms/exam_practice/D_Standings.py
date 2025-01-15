n = int(input())  # Number of log entries
logins = {}

# Process each login from the log
for _ in range(n):
    login = input().strip()  # Read the student login
    if login in logins:
        logins[login] += 1  # Increment problem count for the student
    else:
        logins[login] = 1  # Initialize count for a new student

# Sort by number of problems solved (descending) and by login name (ascending)
sorted_logins = sorted(logins.items(), key=lambda x: (-x[1], x[0]))

# Print the standings table
for login, solved in sorted_logins:
    print(f"{login} {solved}")