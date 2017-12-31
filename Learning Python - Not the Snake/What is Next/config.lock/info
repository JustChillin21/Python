// create a constructor for the StaffMember class
function StaffMember(name,discountPercent){
    this.name=name;
    this.discountPercent=discountPercent;
    }

var sally = new StaffMember("Sally",5);
var bob = new StaffMember("Bob",10);

//Create a StaffMember for yourself called me
var me = new StaffMember("Me",20);

var cashRegister = {
    total:0,
    //Dont forget to add your property
    add: function(itemCost,quantity) {
        lastQuantity=quantity;
        lastTransactionAmount=itemCost*quantity;
        this.total +=  lastTransactionAmount;
    },
    scan: function(item,quantity) {
        switch (item) {
        case "eggs": this.add(0.98,quantity); break;
        case "milk": this.add(1.23,quantity); break;
        case "magazine": this.add(4.99,quantity); break;
        case "chocolate": this.add(0.45,quantity); break;
        }
        return true;
    },
    //Add the voidLastTransaction Method here
    voidLastTransaction: function(){
        this.total-=lastTransactionAmount;
        console.log("Voided: " + lastTransactionAmount+" x "+lastQuantity);
    },
    applyStaffDiscount:function(employee){
        this.name=employee.name;
        discountPercentage=employee.discountPercent/100;
        this.total-=(this.total*discountPercentage);
    }
    
};

cashRegister.scan('eggs',1);
cashRegister.scan('milk',1);
cashRegister.scan('magazine',1);
cashRegister.scan('chocolate',4);

//Void the last transaction and then add 3 instead
cashRegister.voidLastTransaction();
cashRegister.scan('chocolate',3);

//Show the total bill
cashRegister.applyStaffDiscount(me);
console.log('Your bill is '+cashRegister.total.toFixed(2));