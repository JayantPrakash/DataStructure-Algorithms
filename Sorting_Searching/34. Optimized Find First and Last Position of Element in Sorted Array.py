# Run two boundary searches on sorted input: lower bound then upper bound.
# Each discards half the remaining interval, giving O(log n) time and O(1) space.
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
        # Equality moves left too, so start converges to the first value >= target.
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    first = start

    # A lower bound can be past the end or point to a larger value; validate target existence.
    if start == len(nums) or nums[start] != target:
        return [-1,-1]

    end = len(nums) - 1
    while start <= end:
        mid = start + int((end - start) / 2)
        # Now equality moves right: start becomes the first value > target, and end the last <= target.
        if nums[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1

    # Because target existence was confirmed, these two boundaries enclose exactly its duplicate run.
    return [first,end]

array = [5,7,7,8,8,10]
#array = [1,1,2]
array = [5,7,7,8,8,10]
target = 8
print(search(array,target))
