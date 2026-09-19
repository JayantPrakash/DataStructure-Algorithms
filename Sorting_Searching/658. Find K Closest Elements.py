# The intended approach is to locate x in sorted input and expand toward the nearer neighboring values.
# This implementation confuses positions with values, so it is not a correct general k-closest solution.
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
    while start <= end:
        mid = start + int((end-start)/2)
        if nums[mid] == target:
            found_index = mid
            break
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    # Expansion uses the last midpoint, not found_index or a validated insertion boundary; empty input leaves mid undefined.
    i = mid - 1
    j = mid + 1

    count = 1
    output = []

    if mid == -1:
        return nums[0:k]
    # This appends an index instead of nums[mid], mixing an index with the values appended later.
    output.append(mid)
    while len(output) < k:
        # If one side is exhausted, the next candidate must come from the other side.
        if i < 0:
            output.append(nums[j])
            j += 1
            count += 1
            continue
        if j > len(nums) -1:
            output.append(nums[i])
            i -= 1
            count += 1
            continue
        # Distances here are measured from the index mid rather than target x.
        # The output is also in expansion order, not necessarily sorted as the usual problem requires.
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
