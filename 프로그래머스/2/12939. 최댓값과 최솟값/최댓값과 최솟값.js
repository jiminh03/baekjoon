function solution(s) {
    var answer = '';
    
    arr = s.split(' ').map(Number)
    
    // console.log(arr)

    max = Math.max(...arr)
    min = Math.min(...arr)
    
    text = `${min} ${max}`
    
    return text
 
}