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
    while start <= end:
        mid = start + int((end - start)/2)
        if nums[mid] == target:
            start_idx = mid
            break
        elif nums[mid] < target:
            start += 1
        else:
            end -= 1

    if start_idx != -1:
        end_idx = start_idx
        for i in range(start_idx+1,len(nums)):
            if nums[i] == target:
                end_idx += 1
            else:
                break
    if start_idx != -1:
        while start_idx != 0:
            if nums[start_idx - 1] == target:
                start_idx -= 1
            else:
                break

    return [start_idx,end_idx]

array = [5,7,7,8,8,10]
#array = [1,1,2]

print(search(array,8))
