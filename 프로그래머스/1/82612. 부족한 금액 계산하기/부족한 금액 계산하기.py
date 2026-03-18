def solution(price, money, count):
    answer = 0
    cnt = 0
    
    for i in range(1, count+1):
        cnt += price * i

    if cnt <= money:
        answer = 0
    else:
        answer = cnt - money
        
    return answer