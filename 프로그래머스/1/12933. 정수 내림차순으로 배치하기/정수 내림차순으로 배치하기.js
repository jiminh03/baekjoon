function solution(n) {    
    const result = Number(String(n).split('').sort((a, b) => b - a).join(''));
    
    return result;
}