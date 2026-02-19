function solution(s) {
    var answer = '';
    const arr = s.split(" ").map(w => w.toLowerCase())
    
    
    for (let i = 0; i < arr.length; i++){
        if (arr[i] === "")
            continue
        arr[i] = arr[i][0].toUpperCase() + arr[i].slice(1)
        
    }
    
    return arr.join(" ");
}