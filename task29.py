nums = [1, 2, 2, 3, 4, 1, 5, 6, 3, 7]

# result = []
# for num in nums:
#     if nums.count(num) == 1:
#         result.append(num)


result = list(filter(
    lambda num: nums.count(num) == 1,
    nums
))

print(result)
