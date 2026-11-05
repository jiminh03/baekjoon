def solution(left, right):
    count = 0
    
    for i in range(left, right+1):
        sum = 0
        for j in range(1, i+1):
            if i % j == 0:
                sum += 1
                print(i, j, sum)
        if sum % 2 == 0:
            count += i
            print(count)
        else:
            count -= i
    return count