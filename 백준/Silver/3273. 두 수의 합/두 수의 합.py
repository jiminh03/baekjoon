T = input()
arr = list(map(int, input().split()))
num = int(input())

arr.sort()
cnt = 0

l, r = 0, len(arr) - 1

while l < r:
    s = arr[l] + arr[r]
    if s == num:
        cnt += 1
        l += 1
        r -= 1
    elif s < num:
        l += 1
    else:
        r -= 1

print(cnt)