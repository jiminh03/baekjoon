function solution(k, tangerine) {
    var max = Math.max(...tangerine)
    var arr = new Array(max+1).fill(0)
    var sum = 0;
    var cnt = 0;
    
    tangerine.sort((a,b)=> a-b)
    
    for (let i = 0; i < tangerine.length; i++){
        arr[tangerine[i]] += 1
    }
    
    arr.sort((a,b)=> b-a)
    
    for (let i = 0; i < arr.length; i++){
        sum += arr[i]
        cnt += 1
        
        if (sum >= k){
            return cnt;
        }
    }
    }