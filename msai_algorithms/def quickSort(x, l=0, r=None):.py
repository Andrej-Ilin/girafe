import random

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

# Example usage
arr = [3, 6, 8, 10, 1, 2, 4, 5, 7, 9]
sorted_arr = quickSort(arr)
print(sorted_arr)