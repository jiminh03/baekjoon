def solution(n):
    answer = ''
    letter = '수박'
    
    for i in range(n):
        if i % 2 == 0:
            answer += letter[0]
        else:
            answer += letter[1]
    return answer