function solution(n) {
    var cnt = 0;
    
    for (let i = 1; i <= n; i++ ){
        var sum = i
        
        if (i == n){
            cnt += 1
        }
        
        for (let j = i+1; j <= n; j++){
            sum += j
            
            if (sum == n){
                cnt += 1
                break
            }
            else if (sum > n){
                break
            }
        }
    }
    
    return cnt;
}