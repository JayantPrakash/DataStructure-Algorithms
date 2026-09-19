# Binary search on ascending input: [start, end] contains every still-possible target index.
# O(log n) time and O(1) auxiliary space.
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + int((end-start)/2)
        if nums[mid] == target:
            return mid
        # If mid is too small, all positions through mid are too small as well.
        elif nums[mid] < target:
            start = mid + 1
        else:
            # Otherwise mid is too large; exclude it and the entire right half.
            end = mid - 1

    # Bounds crossed without a match, so no candidate remains.
    return -1

array = [-1,0,1,2,3,5,9,10,12]
print(search(array,5))
