def quick_sort(arr):
    length = len(arr)
    if (length == 1):       # if there is only one item in the arr
        return arr
    else:                   # if there are more than one item
        pivot = arr.pop()   # remove the last element from the array and return it

    items_lower = []
    items_greater = []

    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + pivot + quick_sort(items_greater)