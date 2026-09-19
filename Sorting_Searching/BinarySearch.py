# This resembles binary search but advances bounds by one rather than jumping past mid.
# On sorted input it can take O(n) time, despite calculating a midpoint.
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + int((end - start)/2)

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # Only one lower candidate is removed; standard binary search would remove all positions through mid.
            start += 1
        else:
            end -= 1

    return -1

# This sample is not sorted, so binary-search ordering assumptions do not hold in general.
array = [-1,0,3,5,9,1,2]
print(search(array,9))
