function solution(n) {
    var answer = [];
    
    num = String(n)
    
    for (let i = 0; i < num.length; i++){
        answer.push(Number(num.slice(i,i+1)))
    }
    
    return answer.reverse();
}