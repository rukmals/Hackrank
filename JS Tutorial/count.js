/*const o = {
    a: 1,
    b: 2,
    c: 3,
    d: 4
};

console.log('property: value');
// 'p' is the property
for (p in o) {
    console.log(p);
}
let objects = [];
for (i=0;i<5;i++){
    objects.push({x: +(i**2), y: +(i)});
}
console.log(objects);
let count=0;
for (x in objects){
    //console.log(objects[x]);
    var arr = [];
    for (p in objects[x]){
        //console.log(objects[x][p],p);
        arr.push(objects[x][p]);
    }
    //console.log(arr);
    if (arr[0]==arr[1]){
        count+=1;
    }
}
console.log(count);*/
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

/*
 * Return a count of the total number of objects 'o' satisfying o.x == o.y.
 * 
 * Parameter(s):
 * objects: an array of objects with integer properties 'x' and 'y'
 */
function getCount(objects) {
    let count=0;
for (x in objects){
    //console.log(objects[x]);
    var arr = [];
    for (p in objects[x]){
        //console.log(objects[x][p],p);
        arr.push(objects[x][p]);
    }
    //console.log(arr);
    if (arr[0]==arr[1]){
        count+=1;
    }
}return count;
}


function main() {
    const n = +(readLine());
    let objects = [];
    
    for (let i = 0; i < n; i++) {
        const [a, b] = readLine().split(' ');
        
        objects.push({x: +(a), y: +(b)});
    }
    
    console.log(getCount(objects));
}