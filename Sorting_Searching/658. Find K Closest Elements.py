# Key idea: Track how values move toward their final sorted positions.
# Compute or update the search result for the supplied input.
def search(nums, k, x):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    start = 0
    end = len(nums) - 1
    target = x
    found_index = -1
    # Keep processing while `start <= end` remains true.
    while start <= end:
        mid = start + int((end-start)/2)
        # Choose this path when `nums[mid] == target` is true.
        if nums[mid] == target:
            found_index = mid
            break
        # Choose this path when `nums[mid] < target` is true.
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    i = mid - 1
    j = mid + 1

    count = 1
    output = []

    # Choose this path when `mid == -1` is true.
    if mid == -1:
        return nums[0:k]
    output.append(mid)
    # Keep processing while `len(output) < k` remains true.
    while len(output) < k:
        # Choose this path when `i < 0` is true.
        if i < 0:
            output.append(nums[j])
            j += 1
            count += 1
            continue
        # Choose this path when `j > len(nums) - 1` is true.
        if j > len(nums) -1:
            output.append(nums[i])
            i -= 1
            count += 1
            continue
        # Choose this path when `abs(mid - nums[i]) > abs(nums[j] - mid)` is true.
        if abs(mid - nums[i]) > abs(nums[j] - mid):
            output.append(nums[j])
            j += 1
        else:
            output.append(nums[i])
            i -= 1
        count += 1

    return output
array = [-1,0,1,2,3,5,9,10,12]
array = [1,2,3,4,5]
print(search(array,4,3))
