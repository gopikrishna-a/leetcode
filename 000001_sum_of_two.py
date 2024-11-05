# Method - 1

def twoSum(nums, target):
    for x in range(len(nums)):
        for y in range(len(nums)):
            if x != y and nums[x] + nums[y] == target:
                return [x, y]

print(twoSum([3,2,4], 6))



# Method - 2

def twoSum(nums, target):
    for x in range(len(nums)):
        for y in range(x+ 1, len(nums)):
            if x != y and nums[x] + nums[y] == target:
                return [x, y]

print(twoSum([3,2,4], 6))
