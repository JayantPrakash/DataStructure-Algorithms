# Find the upper bound: the first sorted letter strictly greater than target.
# O(log n) time and O(1) space; the letter list must be nonempty.
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

        # Skip equal letters as well as smaller ones because the answer must be strictly greater.
        if nums[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1

    # If start reaches n, modulo wraps to index zero as the problem requires.
    return nums[start % len(nums)]
letters = ["c","f","j"]
letters = ["x","x","y","y"]
target = "z"
array = [-1,0,3,5,9,1,2]
print(search(letters,target))
