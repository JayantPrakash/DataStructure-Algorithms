# After sorting, move inward from the smallest/largest values: O(n log n) overall time.
def twoSum(nums,target):
    # This changes the caller's ordering, so returned positions refer to the sorted array.
    nums.sort()
    i = 0
    j = len(nums) - 1

    while i < j:
        if nums[i] + nums[j] == target:
            # Convert to one-based sorted positions; these are not original input indices.
            return [i+1,j+1]
        # A sum below target can only improve by raising the smaller value; otherwise lower the larger one.
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1

nums = [2,7,11,15]
target = 9

nums = [3,2,4]
target = 6

numbers = [-1,0]
target = -1

numbers = [2,3,4]
target = 6

numbers = [2,7,11,15]
target = 9

numbers = [3,24,50,79,88,150,345]
target = 200

print(twoSum(numbers,target))