import random

def quickSort(x, l=0, r=None, reverse=False):
    if r is None:
        r = len(x)
    if (r - l) > 1:
        pivot = x[random.randint(l, r - 1)]
        less = [i for i in x[l:r] if (i[0] > pivot[0]) or (i[0] == pivot[0] and i[1] < pivot[1])]
        equal = [i for i in x[l:r] if i == pivot]
        greater = [i for i in x[l:r] if (i[0] < pivot[0]) or (i[0] == pivot[0] and i[1] > pivot[1])]
        
        return quickSort(less, 0, len(less)) + equal + quickSort(greater, 0, len(greater))
    return x[::-1] if reverse else x

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    N = int(data[0])

    students = []

    for i in range(1, N + 1):
        line = data[i].split()
        id = int(line[0])
        score = int(line[1])
        nickname = line[2]
        students.append((score, id, nickname))

    # Sort students using quickSort
    sorted_students = quickSort(students)

    # Output the top three nicknames
    for i in range(3):
        print(sorted_students[i][2])

    # Output the sorted IDs
    sorted_ids = [str(student[1]) for student in sorted_students]
    print(" ".join(sorted_ids))

# Ensure the script is run correctly
if __name__ == "__main__":
    main()
