def binary_search(numbers_list, number_to_find):
    start_index = 0
    end_index = len(numbers_list) - 1

    while start_index <= end_index:     # if the array is a valid array
        middle_index = (start_index + end_index) // 2

        if numbers_list[middle_index] == number_to_find:   # if the target equal to the current middle number
            return middle_index
        elif numbers_list[middle_index] < number_to_find:   # if the target is greater than the current middle number
            start_index = middle_index + 1     # ignore the left array
        else:   # if the target is less than the current middle number
            end_index = middle_index - 1     # ignore the right array
    
    return -1   # return -1 when number no found
        