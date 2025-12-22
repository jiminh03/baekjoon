import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
arr = deque()

for _ in range(T):
    text = input().strip()

    if text.startswith("push"):
        arr.append(text[5:])
    elif text == "front":
        if arr:
            print(arr[0])
        else:
            print('-1')
    elif text == "back":
        if arr:
            print(arr[len(arr)-1])
        else:
            print('-1')
    elif text == "empty":
        if arr:
            print('0')
        else:
            print('1')
    elif text == "size":
        print(len(arr))
    elif text == "pop":
        if arr:
            a = arr.popleft()
            print(a)
        else:
            print('-1')