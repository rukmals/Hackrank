function isPositive(s){
    try{
        if (s>=0) throw "YES";
        if (s==0) throw "Zero Error";
        if (s<0) throw "Negative Error";

    }catch(e){
        return e;
    }
    
}
/*console.log(isPositive(1));
console.log(isPositive(0));
console.log(isPositive(-1));
console.log(isPositive(10));*/

/*'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});



/*
 * Complete the isPositive function.
 * If 'a' is positive, return "YES".
 * If 'a' is 0, throw an Error with the message "Zero Error"
 * If 'a' is negative, throw an Error with the message "Negative Error"
 */
/*function isPositive(a) {
    
}

function main() {
    const n = +(readLine());
    
    for (let i = 0; i < n; i++) {
        const a = +(readLine());
      
        try {
            console.log(isPositive(a));
        } catch (e) {
            console.log(e.message);
        }
    }
}*/
