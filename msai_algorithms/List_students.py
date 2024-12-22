
logins = set()
n = int(input())
for _ in range(n):
    login = input().split()
    print(login)
    logins.add(login)
print(len(logins))