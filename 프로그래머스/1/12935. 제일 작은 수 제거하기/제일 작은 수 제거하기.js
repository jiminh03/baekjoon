function solution(arr) {
    var answer = [];
    
    var min = Math.min(...arr)
    var idx = arr.indexOf(min)
    
    arr.splice(idx, 1)
    
    if (arr.length == 0){
        return [-1]
    }
    
    return arr;
}