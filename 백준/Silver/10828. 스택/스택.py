import sys
input = sys.stdin.readline

T = int(input())
arr = []

for _ in range(T):
    text = input().strip()

    if text.startswith("push"):
        arr.append(int(text[5:]))

    elif text == "size":
        print(len(arr))

    elif text == "top":
        if arr:
            print(arr[len(arr)-1])
        else:
            print('-1')

    elif text == "empty":
        if arr:
            print('0')
        else:
            print('1')
    else:
        if arr:
            num = arr.pop()
            print(num)
        else:
            print('-1')

