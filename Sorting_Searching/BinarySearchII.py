# Key idea: Track the search interval and the condition that discards half of it.
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
        mid = start + int((end-start)/2)
        # Choose this path when `nums[mid] == target` is true.
        if nums[mid] == target:
            return mid
        # Choose this path when `nums[mid] < target` is true.
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1

array = [-1,0,1,2,3,5,9,10,12]
print(search(array,5))
