function solution(s)
{
    var answer = 0;
    var stack = [];
    
    for (let i = 0; i < s.length; i++){
        
        var now = s.slice(i, i+1)
        
        var last = stack[stack.length - 1]
        
        if (stack.length > 0 && now === last){
            stack.pop()
        }
        else{
            stack.push(now);
        }
        
    }
    
            
    if (stack.length == 0){
        answer = 1;
    }
    
    return answer;
}