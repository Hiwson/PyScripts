// js classes
// we use the "class" keyword to create a class
class student{
  constructor(name,course,age){ //its a must to include "constructor"
    this.name = name;
    this.course = course;
    this.age = age;
  }
}

let stud1 = new student("Elsa","Beauty",24);
let stud2 = new student("Mwadibo","ICT",20);
console.log(stud1);
console.log(stud2);

class school{
  constructor(name,type,startYr){
    this.name = name;
    this.type = type;
    this.startYr = startYr;
  }
  comment(){
    console.log(`This ${this.name} is an ${this.type} which was started on ${this.startYr}`)
  }
}
let institution = new school("JKUAT","Agriculture",1966);
console.log(institution.name);
console.log(institution.comment());

//class inheritance

class adm extends school{
  constructor(name,type,startYr,year){
    super(name,type,startYr);
    this.admYr = year;
  }
  say(){
    return this.comment() + ", and am in " + this.yr;
  }
}
 let detail = new adm("MMU","Tech",1968,2025);
console.log(detail)

