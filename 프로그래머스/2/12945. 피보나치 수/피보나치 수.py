def solution(n):
    answer = 0
    
    if n == 2:
        answer = 1
    elif n == 3:
        answer = 2
    else:
        first = 1
        second = 2
        
        for i in range(4, n+1):
            answer = (first+second)%1234567
            first = second
            second = answer
    
    return answer