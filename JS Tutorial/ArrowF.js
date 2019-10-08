/*const arr = [1, 2, 3, 4, 5];

const sum = arr.reduce((a, b) => { return a + b }, 0);

console.log('Array:', arr);
console.log('Sum:', sum);*/
/*function modifyArray(nums) {
    const modifyarray = (nums)=>{return nums}
//return modifyarray;
    
}
const arr = [1, 2, 3, 4, 5];

const greaterThan3 = arr.filter(function(a) {
    return a > 3;
});

console.log('Array:', arr);
console.log('Elements Greater Than 3:', greaterThan3);*/
function modifyArray(nums){
    var a = nums;
    var modifyarray = (a)=>{
        var x = 0;
        for (i=0;i<a.length;i++){
            if(a[i]%2!=0){
                a[i]=a[i]*3;
            }else{
                a[i]=a[i]*2;
            }
            //x+=i;
        }
        return a;
        
        //return a}
    }
   //return a;
    return modifyarray(a);
}


console.log(modifyArray([1,2,3,4,5]));
/*const makeArray = (...values) => { return values };
console.log('Array:', makeArray(1, 2, 3, 4));
console.log('Array:', makeArray(1, 2, 3, 4, 5, 6));*/
