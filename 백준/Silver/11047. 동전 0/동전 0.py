N, K = map(int, input().split())
arr = []
cnt = 0

for _ in range(N):
    A = int(input())
    if A <= K:
        arr.append(A)

for i in range(len(arr)-1, -1, -1):
    if K >= arr[i]:
        cnt += K // arr[i]
        K = K % arr[i]
    else:
        continue

print(cnt)