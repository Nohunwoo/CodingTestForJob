n = int(input())
nums = list(map(int, input().split()))

answer = 0
nums.sort()
for i in range(len(nums)):
    answer += nums[i] * (i - (n -1 - i))

print(answer*2)