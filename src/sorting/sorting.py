# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    left_array = 0
    right_array = 0
    # Your code here
    for i in range(elements):
        if left_array >= len(arrA):
            merged_arr[i] = arrB[right_array]
            right_array += 1
        elif right_array >= len(arrB):
            merged_arr[i] = arrA[left_array]
            left_array += 1
        #
        elif arrA[left_array] < arrB[right_array]:
            merged_arr[i] = arrA[left_array]
            left_array += 1
        else:
            merged_arr[i] = arrB[right_array]
            right_array += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) < 1:
        return arr
    else:
         midpoint = len(arr) // 2
         left_side = arr[:midpoint]
         right_side = arr[midpoint:]

    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    return merge(left_side,right_side)

    #return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
#def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

