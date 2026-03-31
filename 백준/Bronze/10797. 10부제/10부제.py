num = int(input())
car = list(map(int, input().split()))
cnt = 0

for i in car:
    if num == i:
        cnt += 1

print(cnt)