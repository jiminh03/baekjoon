def solution(s):
    cnt = 0
    repeat = 0

    for _ in range(len(s)):
        if s == '1':
            break

        remove = ''

        for i in s:
            if i == '1':
                remove += i
            else:
                cnt += 1

        s = bin(len(remove))[2:]
        repeat += 1

    answer = [repeat, cnt]
    return answer