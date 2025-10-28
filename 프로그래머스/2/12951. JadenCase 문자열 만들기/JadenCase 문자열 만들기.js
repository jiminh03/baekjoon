function solution(s) {
    var answer = '';
    var arr = [];
    
    arr = s.split(' ').map(String)
    console.log(arr)
    
    for (let i = 0; i < arr.length; i++){
        
        if (i != arr.length - 1){
            answer += arr[i].slice(0,1).toUpperCase() + arr[i].slice(1,arr[i].length).toLowerCase() + ' '
        }
        else{
            answer += arr[i].slice(0,1).toUpperCase() + arr[i].slice(1,arr[i].length).toLowerCase() 
        }
        
    }
    
    return answer;
}