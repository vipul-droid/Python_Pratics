nums = (2,4,6,8)


print(nums)
print(type(nums))

# for i in range(len(nums)):
#     print(nums[i])

# for num in nums:
#     print(num)

temp = list(nums)

temp[2] = 9
nums = tuple(temp)
print(nums)