# Key idea: Track how values move toward their final sorted positions.
# Compute or update the search result for the supplied input.
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    start = 0
    end = len(nums) - 1

    start_idx = -1
    end_idx = -1
    # Keep processing while `start <= end` remains true.
    while start <= end:
        mid = start + int((end - start)/2)
        # Choose this path when `nums[mid] == target` is true.
        if nums[mid] == target:
            start_idx = mid
            break
        # Choose this path when `nums[mid] < target` is true.
        elif nums[mid] < target:
            start += 1
        else:
            end -= 1

    # Choose this path when `start_idx != -1` is true.
    if start_idx != -1:
        end_idx = start_idx
        # Process each value from `range(start_idx + 1, len(nums))`.
        for i in range(start_idx+1,len(nums)):
            # Choose this path when `nums[i] == target` is true.
            if nums[i] == target:
                end_idx += 1
            else:
                break
    # Choose this path when `start_idx != -1` is true.
    if start_idx != -1:
        # Keep processing while `start_idx != 0` remains true.
        while start_idx != 0:
            # Choose this path when `nums[start_idx - 1] == target` is true.
            if nums[start_idx - 1] == target:
                start_idx -= 1
            else:
                break

    return [start_idx,end_idx]

array = [5,7,7,8,8,10]
#array = [1,1,2]

print(search(array,8))
