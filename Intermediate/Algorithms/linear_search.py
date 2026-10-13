# 1. Linear search starts at the beginning of a list and iterates through each item until it finds the target value looking for.
#when the target is found the index where it's located in the list is returned if not found it returns.
#if not found it returns -1

def linear_search(arr,target):
    for i in range (len(arr)):
        if arr[i] == target:
            return i
    return -1
#The time complexity of linear search is 0(n) because the time it takes to search through the list grows linearly with the size of the list.
#The space complexity of liner search is 0(1) because it don't require any additional space to search through the list.

# 2. Binary search is a more efficient algorithm for searching through a list of items.
#The condition is that the list must be sorted in ascending order.
#Binary search works by dividing the list in half and checking if the target value is in the middle of the list, the index of the target is returned. otherwise the algorith checks if the target value is in the left or right half of the list if no target value it returns -1.
