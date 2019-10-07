class Polygon {
    constructor(list) {
        this.list = list;
        //this.x=list.length;
    }
    perimeter(){
        if(this.list.length==4 & this.list[0]==this.list[1]){
            return 4*this.list[0];

        }else if(this.list.length==4 & this.list[0]<this.list[1]){
            return 2*(this.list[0]+this.list[1]);
        }else if(this.list.length==5){
            return this.list[0]+this.list[1]+this.list[2]+this.list[3]+this.list[4];
        }
    }
    

}
/*function getHeiht(x){
    return x;
}*/

//let p = new Polygon(1, 2);
//console.log(p.getHeiht(2));
const rectangle = new Polygon([10, 20, 10, 20]);
const square = new Polygon([10, 10, 10, 10]);
const pentagon = new Polygon([10, 20, 30, 40, 43]);

console.log(rectangle.perimeter());
console.log(square.perimeter());
console.log(pentagon.perimeter());
/*class Car {
    constructor(brand) {
      this.carname = brand;
    }
    present(x) {
      return x + ", I have a " + this.carname;
    }
  }
  
  mycar = new Car("Ford");
  document.getElementById("demo").innerHTML = mycar.present("Hello");*/