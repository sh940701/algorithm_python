nums = input().split()

print(max(int(nums[0][::-1]), int(nums[1][::-1])))
