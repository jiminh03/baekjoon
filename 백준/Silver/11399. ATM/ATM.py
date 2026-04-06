N = int(input())
arr = list(map(int, input().split()))
cnt = 0

arr.sort()

for i in range(len(arr)):
    cnt += arr[i] * (N-i)

print(cnt)