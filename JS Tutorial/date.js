function getDayName(dateString) {
    var dayName;
    var month = dateString.slice(0,2)-1;
    var day = dateString.slice(3,5);
    var year = dateString.slice(6,10);
    var d0=new Date(year,month,day);
    var number = d0.getDay();
    switch(number){
         case(0):
            dayName = "Sunday";
            break;
        case(1):
             dayName="Monday";
            break;
        case(2):
             dayName="Tuesday";
            break;
        case(3):
             dayName = "Wednesday";
            break;
        case(4):
             dayName= "Thursday";'use strict';

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

// The days of the week are: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
function getDayName(dateString) {
    var dayName;
    var month = dateString.slice(0,2)-1;
    var day = dateString.slice(3,5);
    var year = dateString.slice(6,10);
    var d0=new Date(year,month,day);
    var number = d0.getDay();
    switch(number){
         case(0):
            dayName = "Sunday";
            break;
        case(1):
             dayName="Monday";
            break;
        case(2):
             dayName="Tuesday";
            break;
        case(3):
             dayName = "Wednesday";
            break;
        case(4):
             dayName= "Thursday";
            break;
        case(5):
             dayName = "Friday";
            break;
        case(6):
             dayName = "Saturday";
            break;
       
        
        
    }
    return dayName;
}

function main() {
    const d = +(readLine());
    
    for (let i = 0; i < d; i++) {
        const date = readLine();
        
        console.log(getDayName(date));
    }
}
            break;
        case(5):
             dayName = "Friday";
            break;
        case(6):
             dayName = "Saturday";
            break;
       
        
        
    }
    return dayName;
}
console.log(getDayName("10/13/2019"));