n = int(input())

tri = [0,1]
nums = [0,1]
i = 1

while True:
    tri.append(tri[i] + (i+1))
    nums.append(nums[i] + tri[i+1])
    if nums[-1] >= n:
        break
    i += 1

cnt = [100000000]*(n+1)
cnt[0] = 0

for i in range(1,n+1):
    for num in nums:
        if num <= i : cnt[i] = min(cnt[i-num] + 1, cnt[i])
        else: break

print(cnt[n])