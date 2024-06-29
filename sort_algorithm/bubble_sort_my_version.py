# best case: O(n), everything is sorted
# worst case: O(n^2), everything needs to be sorted

def bubble_sort(array):
    length = len(array)
    sorted = False

    while not sorted:
        sorted = True
        for index, item in enumerate(array):

            # if item is not last item and next item is less than current item
            if index < length - 1 and item > array[index + 1]:
                
                # swap the current and next item
                array[index], array[index + 1] = array[index + 1], array[index]
                sorted = False

    return array

elements = [5, 9, 2, 1, 67, 34, 88, 34]

print(bubble_sort(elements))

        


