def find_duplicate(nums):
    nums.sort()
    if nums is str or nums is None:
        return False
    else:
        for index in range(len(nums) - 1):
            if nums[index] == nums[index + 1]:
                if nums[index] < 0:
                    return False
                else:
                    return nums[index]
    return False
