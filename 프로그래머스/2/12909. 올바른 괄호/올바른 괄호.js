function solution(s){
    var answer = true;

    const arr = s.split("")
    let cnt = 0
    
    for (let i = 0; i < arr.length; i++){
        if (arr[i] == '('){
            cnt ++;
        }
        else{
            cnt --;
        }
        
        if (cnt < 0){
            answer = false;
        }
    }
    
    if (cnt !== 0){
        answer = false;
    }

    return answer;
}