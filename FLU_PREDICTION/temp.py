def erase_in_non_decreasing_order(arr):
    def find_next_min_index(start, arr):
        min_val = float('inf')
        min_index = -1
        for i in range(start, len(arr)):
            if arr[i] < min_val:
                min_val = arr[i]
                min_index = i
        return min_index

    operations = 0
    p = 0
    pop_cnt=0
    while arr:
        next_min_index = find_next_min_index(p, arr)
        # Increment or decrement pointer to reach next minimum element
        while p != next_min_index:
            if p < next_min_index:
                p += 1  # Increment pointer
            else:
                p -= 1  # Decrement pointer
            operations += 1
        # Erase the element
        arr.pop(p)
        
        operations += 1
        # Choose where to point p after erasing the element
        if p == len(arr):  # If p is at the end, move it to the previous element
            p -= 1
        # No need to move p if it's not at the end as it will automatically point to the next element

    return operations

# Example usage:
A = [1]
print(erase_in_non_decreasing_order(A))
