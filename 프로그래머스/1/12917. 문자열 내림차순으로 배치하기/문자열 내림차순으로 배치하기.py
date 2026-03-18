def solution(s):
    answer = ''
    arr = [''] * 123
    
    for i in s:
        arr[ord(i)] += i
        
    for i in range(len(arr)):
        if arr[i] != 0:
            answer += arr[i]
    
    return ''.join(reversed(answer))