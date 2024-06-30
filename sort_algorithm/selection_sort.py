# loop through the arr, finding the smallest element in the arr and put it in the front
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i  # set the first element as the temporary smallest index
        for j in range(i + 1, len(arr)): # loop through the rest of the element
            if arr[j] < arr[min_index]:  # if an element in the rest of the list is smaller than the temporary smallest element
                min_index = j # update the minimal index
        arr[i], arr[min_index] = arr[min_index], arr[i]  # swap the element
    return arr 
  