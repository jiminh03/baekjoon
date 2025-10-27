const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    let result = '';
    
    for (const ch of str){
        if(ch >= 'A' && ch <= 'Z')
           result += ch.toLowerCase() 
        else
            result += ch.toUpperCase()
    }

    console.log(result)
});