class Animal {
    constructor(name) {
        this.name = name;
    }
    speak() {
        console.log(this.name, 'speaks.');
    }
}

class Dog extends Animal {
    speak() {
        console.log(this.name, 'barks.');
    }
}

let spot = new Dog('Spot');
spot.speak();

spot = new Animal('Spot');
spot.speak();

class Rectangle {
    constructor(w, h) {
        this.w = w;
        this.h = h;
    }

}
Rectangle.prototype.area=function(){
    return this.w*this.h;
}
class Square extends Rectangle{
    constructor(w){
        super(w);
    }
    
}
Square.prototype.area=function(){
    return this.w**2;
}
//if (JSON.stringify(Object.getOwnPropertyNames(Square.prototype)) === JSON.stringify([ 'constructor' ])) {
    const rec = new Rectangle(3, 4);
    const sqr = new Square(3);
    
    console.log(rec.area());
    console.log(sqr.area());
//} else {
   /* console.log(-1);
    console.log(-1);
}*/