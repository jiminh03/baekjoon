while True:
    text = input().lower()
    if text == '#':
        break

    cnt = 0
    cnt += text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u')

    print(cnt)
