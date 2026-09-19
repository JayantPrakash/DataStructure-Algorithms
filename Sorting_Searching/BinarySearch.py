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
            start += 1
        else:
            end -= 1

    return -1

array = [-1,0,3,5,9,1,2]
print(search(array,9))
