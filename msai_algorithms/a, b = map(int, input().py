# a, b = map(int, input().split())
# print(a + b)

"Selection Sort O(N**2)"
x = [4, 2, 5, 6, 3, 8, 7, 1]
N = len(x)
for i in range(N-1) :
    i_min = i
    for j in range(i+1, N) :
        if x[j] < x[i_min] :
             i_min = j
    x[i], x[i_min] = x[i_min], x[i]
print(x)

"Insertion Sort O(N**2)"
x = [4, 2, 5, 6, 3, 8, 7, 1]
for i in range(1, len(x)) :
    key = x[i]
    j = i - 1
    while j >= 0 and key < x[j] :
        x[j+1] = x[j]
        j -= 1
    x[j+1] = key
print(x)

"Bubble Sort O(N**2)"
x = [4, 2, 5, 6, 3, 8, 7, 1]
N = len(x)
for i in range(N-1) :
     for j in range(0, N-i-1) :
          if x[j] > x[j+1] :
               x[j], x[j+1] = x[j+1], x[j]

print(x)

def merge(x, l, m, r):
    temp = []
    i1 = l
    i2 = m
    while i1 < m and i2 < r:
        if (i2 >= r) or ((i1 < m) and (x[i1] < x[i2])):
            temp.append(x[i1])
            i1 += 1
        else:
            temp.append(x[i2])
            i2 += 1
    # Add remaining elements from the left half
    while i1 < m:
        temp.append(x[i1])
        i1 += 1
    # Add remaining elements from the right half
    while i2 < r:
        temp.append(x[i2])
        i2 += 1
    x[l:r] = temp

def merge_sort(x, l=0, r=None):
    if r is None:
        r = len(x)
    if r - l > 1:
        m = (l + r) // 2
        merge_sort(x, l, m)
        merge_sort(x, m, r)
        merge(x, l, m, r)
    return x  # Return the sorted array

print(merge_sort([4, 2, 5, 6, 3, 8, 7, 1]))

"Quick Sort O(N**2)"
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
print(quick_sort([4, 2, 5, 6, 3, 8, 7, 1]))