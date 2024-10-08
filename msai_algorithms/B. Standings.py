import sys
import random
with open('./girafe/msai_algorithms/file.txt', 'r') as f:
    data = f.read().strip().split('\n')
# print(data)

N = int(data[0])

student = {}

def quickSort(x, l=0, r=None):
    if r is None:
        r = len(x)  # Adjust this to include the last element in the range
    if (r - l) > 1: # Ensure that there are at least two elements to sort
        pivot = x[random.randint(l, r - 1)]
        less = [i for i in x[l:r] if i < pivot]  # Elements less than pivot
        equal = [i for i in x[l:r] if i == pivot]  # Elements equal to pivot
        greater = [i for i in x[l:r] if i > pivot]  # Elements greater than pivot
        
        # Recursively sort the less and greater parts and combine them
        return quickSort(less, 0, len(less)) + equal + quickSort(greater, 0, len(greater))
    return x  # Return the sorted elements

# read of the data
list_score = []

for i in range(1, N + 1):
    line = data[i].split()
    # print(line)
    id = int(line[0])
    score = int(line[1])
    list_score.append(score)
    nickname = line[2]
    student[score] = [id, nickname]
# print(student.get())
# print(quickSort(list_score)[::-1])
sort_score = quickSort(list_score)[::-1]
top_3_nickname = []

for i in sort_score[:3]:
    top_3_nickname.append(student.get(i)[1])
print(top_3_nickname)
