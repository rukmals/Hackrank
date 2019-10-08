/*-------------------------------------------------
console.log("first line\n" + "second line");
console.log("first line" + "\nsecond line");
console.log("first line\"second line");*/
//--------------------------------------------------------
/*
console.log(`first line
second line`);
*/
//-------------------------------------------------
/*
const a = 2;
const b = 3;

console.log(
    'The sum of a and b is ' + (a + b) + '.\n' 
    + 'The product of a and b is ' + (a * b) + '.'
);
*/
//-----------------------------------------------------------
/*
var a = 5;
var b = 10;

function foo(strings, ...values) {
    console.log("." + strings[0] + ".");
    console.log("." + strings[1] + ".");
    console.log( strings[2] + ".");
    //.log("." + strings[3] + ".");
    console.log(values[0]);
    console.log(values[1]);
    console.log(values[2]);
}

foo`Sum ${a + b}
Product ${a * b}
Division ${b / a}`;
*/
//-------------------------------------------
var a = 5;
var b = 10;

function foo(strings, ...values) {
    let a = values[0];
    let b = values[1];

    return `Sum ${a + b}
Product ${a * b} 
Division ${b / a}`;
}

console.log(foo`Num1 ${a + 10}
Num2 ${b * 2} 
Num3 ${b / a}`);


function sides(literals, ...expressions) {
    var arr = [];
    let a = expressions[0];
    let p = expressions[1];
    var s_1 = (p+Math.sqrt((p**2)-16*a))/4;
    var s_2 = (p-Math.sqrt((p**2)-16*a))/4;
    arr.push(s_1);
    arr.push(s_2);
    arr.sort();
    return arr;

    
}
var s1=10;
var s2=14;
const [x, y] = sides`The area is: ${s1 * s2}.\nThe perimeter is: ${2 * (s1 + s2)}.`;
 console.log(x); 
console.log((s1 === x) ? s1 : -1);
console.log((s2 === y) ? s2 : -1);

/*
'use strict';

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

function readLine() {
    return inputString[currentLine++];
}

function sides(literals, ...expressions) {
    
}


function main() {
    let s1 = +(readLine());
    let s2 = +(readLine());
    
    [s1, s2] = [s1, s2].sort();
    
    const [x, y] = sides`The area is: ${s1 * s2}.\nThe perimeter is: ${2 * (s1 + s2)}.`;
    
    console.log((s1 === x) ? s1 : -1);
    console.log((s2 === y) ? s2 : -1);
}*/