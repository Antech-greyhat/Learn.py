# Divide and conquer is a technique for recursively breaking down problems into smaller sub problems.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    sorted_list = []
    i =0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

#The time complexity for merge sort would be 0(n log n) because the list is continuously divided in half (log n) and then merged together (0(n)) and space complexity of 0(n)