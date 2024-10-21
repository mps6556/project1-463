# maximum_subarray.py

def max_subarray(arr):
    max_ending_here = max_so_far = arr[0]
    start = end = s = 0

    # Kadane's algorithm
    for i in range(1, len(arr)):
        # check if it's better to start a new subarray
        if arr[i] > max_ending_here + arr[i]:
            max_ending_here = arr[i]
            s = i

        # continue the subarray
        else:
            max_ending_here += arr[i]

        # check
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = s
            end = i

    return max_so_far, start, end
