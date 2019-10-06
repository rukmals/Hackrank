//import { reverse } from "dns";

function GetVowel(s){
    var vowel = '';
    for (i=0;i<s.length;i++){
        if (s[i]=='a'|| s[i]=='e'|| s[i]=='i'|| s[i]=='o'|| s[i]=='u' ){
            //vowel.push(s[i]);
            //vowel+=s[i];
            console.log(s[i]);

        }
    }
    for (i=0;i<s.length;i++){
        if (s[i]!='a' & s[i]!='e'& s[i]!='i'& s[i]!='o'& s[i]!='u' ){
            //vowel.push(s[i]);
            //vowel+=s[i];
            console.log(s[i]);

        }
    }
    //return vowel
}
//console.log(GetVowel("asgjfnidbhobaebv"));
//GetVowel("javascripts");
function Factorial(n){
    var x =1 ;
    for(i=1;i<n+1;i++){
        x=x*i
    }
    return x;
}

//console.log(Factorial(5));
/*console.log(Math.PI);
const x =4;
console.log(x);
*/
function getGrade(score) {
    let grade;
    if (1<=score & score<=30){
        if(1<=score & score<5){
            grade = "F";
        }else if(5<score & score<=10){
            grade = "E";
        }else if(10<score & score<=15){
            grade = "D";
        }else if(15<score & score<=20){
            grade = "C";
        }else if(20<score & score<=25){
            grade = "B";
        }else{
            grade = "A";
        }
    }return grade;
   
}
//console.log(getGrade(11));
//getGrade(15);
function getLetter(word){
    var x = word.charAt(0);
    switch(x){
        case 'a':
            return "A";
            break;
        case 'e':
            return "B";
            break;
        case 'i':
            return "C";
            break;
        case 'o':
            return "D";
            break;
        case 'u':
            return "A";
            break;
        case 'b':
            return "B";
            break;
        case 'c':
            return "B";
            break;
        case 'd':
            return "B";
            break;
        case 'f':
            return "B";
            break;
        case 'g':
            return "B";
            break;
        case 'h':
            return "C";
            break;
        case 'j':
            return "C";
            break;
        case 'k':
            return "C";
            break;
        case 'l':
            return "C";
            break;
        case 'm':
            return "C";
            break;
        default:
            return "D";
    }
}
//console.log(SW("nbhkefw"))
function getSecondLargest(nums) {
    // Complete the function
    //nums.sort();
    //return nums.indexOf(12);
    nums.sort(function(a,b){return a-b});
    return nums[nums.indexOf(nums[nums.length-1])-1];

    
}
//console.log(getSecondLargest([1,2,3,4,1,2,12,1,2,1,1,1,12,12,12,12]));

function reverseString(str){
    var str_1=str;
    try{
       str_2 = str.split( '' );
       console.log(str_2.reverse().join( '' ));
    }catch(e){
        console.log(e.message);
        console.log(str_1);
    }finally{
        //console.log(str_1.reverse().join( '' ));
        //console.log(str_1);
        
    }
   
}
//console.log(reverseString(Number(1234)));
//reverseString("1234");
//reverseString(Number(1234));
/*var a =1;
//var p =2;
try{
    b=1/p;
    console.log(`new value of a is   `+a);
}catch(e){
    console.log(e.message);
    console.log(a);
}finally{
    b=1/p;
    console.log(b);
}*/
/*function isPositive(a){
    try{
        if (a>0) throw "YES";
        if (a==0) throw "Zero Error";
        if (a<0) throw "Negative Error";
    }catch(e){
        return e;
    }
   
  
}
console.log(isPositive(1));
console.log(isPositive(0));
console.log(isPositive(-1));
console.log(isPositive(100));*/
/*function Rectangle(a, b) {
    this.length = a;
    this.width = b;
    this.perimeter = 2*(a+b);
    this.area = a*b;

}


const rec = new Rectangle(2, 4);
    
console.log(rec.length);
console.log(rec.width);
console.log(rec.perimeter);
console.log(rec.area);*/
let objects = [];
for(i=0;i<10;i++){
    var a=i*2;
    var b=i;
    objects.push({x: +(a), y: +(b)});
}

console.log(objects);
var keys =[]
for (p in objects){
    console.log(p,objects[p][0]);
}