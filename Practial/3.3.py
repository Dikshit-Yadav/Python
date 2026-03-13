def find_max_min(nums):
    maximum = max(nums)
    minimum = min(nums)
    return (maximum, minimum)

nums = [10, 5, 25, 7, 2]
print("Max and Min:", find_max_min(nums))
