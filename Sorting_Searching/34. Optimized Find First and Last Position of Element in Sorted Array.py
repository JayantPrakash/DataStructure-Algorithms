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

    # Keep processing while `start <= end` remains true.
    while start <= end:
        mid = start + int((end - start)/2)
        # Choose this path when `nums[mid] < target` is true.
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    first = start

    # Choose this path when `start == len(nums) or nums[start] != target` is true.
    if start == len(nums) or nums[start] != target:
        return [-1,-1]

    end = len(nums) - 1
    # Keep processing while `start <= end` remains true.
    while start <= end:
        mid = start + int((end - start) / 2)
        # Choose this path when `nums[mid] <= target` is true.
        if nums[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1

    return [first,end]

array = [5,7,7,8,8,10]
#array = [1,1,2]
array = [5,7,7,8,8,10]
target = 8
print(search(array,target))
