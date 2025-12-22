arr = []

for _ in range(10):
    T = int(input())
    arr.append(T%42)

print(len(set(arr)))
