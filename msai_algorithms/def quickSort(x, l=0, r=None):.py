import random

with open('./girafe/msai_algorithms/input.txt', 'r') as f:
    data = f.read().strip().split('\n')

def quickSort(x, l=0, r=None, reverse=False):
    if r is None:
        r = len(x)  # Adjust this to include the last element in the range
    if (r - l) > 1:  # Ensure that there are at least two elements to sort
        pivot = x[random.randint(l, r - 1)][1]  # Use the value of the tuple as the pivot
        less = [i for i in x[l:r] if i[1] < pivot]  # Elements less than pivot
        equal = [i for i in x[l:r] if i[1] == pivot]  # Elements equal to pivot
        greater = [i for i in x[l:r] if i[1] > pivot]  # Elements greater than pivot
        
        # Recursively sort the less and greater parts and combine them
        return quickSort(less, 0, len(less)) + equal + quickSort(greater, 0, len(greater))
    return x  # Return the sorted elements

N = int(data[0])
print(N)
print(list(map(int, data[1].split())))
x = list(map(int, data[1].split()))

print(quickSort(x))