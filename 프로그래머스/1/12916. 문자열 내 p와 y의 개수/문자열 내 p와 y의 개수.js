function solution(s){
    var answer = true;
    var countp = 0;
    var county = 0;
    
    s = s.toLowerCase();
    
    for (let i = 0; i < s.length; i++){
        if (s[i] == 'p'){
            countp += 1
        }
        else if (s[i] == 'y'){
            county += 1
        }
    }
    
    if (countp != county){
        answer = false
    }
    
    return answer;
}