T = int(input())
cnt = 0

for tc in range(1, T+1):
    text = input()
    value = True


    for i in range(len(text) - 1):
        if text[i] != text[i + 1] and text[i] in text[i + 1:]:
            value = False
            break

    if value:
        cnt += 1
    

print(cnt)
