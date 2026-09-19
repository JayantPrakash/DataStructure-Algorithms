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

        if nums[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1

    return nums[start % len(nums)]
letters = ["c","f","j"]
letters = ["x","x","y","y"]
target = "z"
array = [-1,0,3,5,9,1,2]
print(search(letters,target))
