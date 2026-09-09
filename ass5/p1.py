nums = [1, 1, 2, 2, 3]

j = 0

for i in range(1, len(nums)):
    if nums[i] != nums[j]:
        j += 1
        nums[j] = nums[i]

print("Length:", j + 1)
print("Array:", nums[:j + 1])