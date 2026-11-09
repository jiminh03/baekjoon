def solution(n):
    
    count = bin(n).count('1')
    num = n+1
    
    while bin(num).count('1') != count:
        num += 1
    
    return num