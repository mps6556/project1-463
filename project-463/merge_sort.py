# merge_sort.py

def merge_sort(arr, key=None):
    # Base case
    if len(arr) <= 1:
        return arr

    # Split the array in half
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key=key)
    right = merge_sort(arr[mid:], key=key)
    return merge(left, right, key)

# Merge function
def merge(left, right, key=None):
    result = []
    i = j = 0

    # Compare elements in both arrays
    while i < len(left) and j < len(right):
        # Check if a key is provided
        if key:
            if left[i][key] <= right[j][key]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # If no key is provided, compare the elements directly
        else:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    # Add the remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result
