def solution(s):
    answer = True
    
    for i in s:
        if i.isalpha() or (len(s) != 4 and len(s) != 6):
            answer = False
    
    return answer