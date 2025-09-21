import sys

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

arr.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end = 0

for s, e in arr:
    if s >= last_end:
        count += 1
        last_end = e

print(count)