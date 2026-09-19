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
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    first = start

    if start == len(nums) or nums[start] != target:
        return [-1,-1]

    end = len(nums) - 1
    while start <= end:
        mid = start + int((end - start) / 2)
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
