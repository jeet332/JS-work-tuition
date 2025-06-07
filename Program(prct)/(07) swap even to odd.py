# n=[2,3,4,5,6,7,8,8,]
# if n%2==0:
#     print("odd",n)
# elif n%2!=0:
#     print("even",n)


# Pehle se hi ek list bana lo
nums = [10, 20, 30, 40, 50, 60]

# List ki length nikal lo
n = len(nums)

# Even-odd position par swapping karo
i = 0
while i < n - 1:
    temp = nums[i]
    nums[i] = nums[i + 1]
    nums[i + 1] = temp
    i += 2

# Final result print karo
print("List after swapping:", nums)
