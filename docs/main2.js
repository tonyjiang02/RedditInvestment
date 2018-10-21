
var config = {
    apiKey: "AIzaSyCKqrBhHXZoUdznArZzgLvvpRSGHc6nDok",
    authDomain: "hshacks-investment.firebaseapp.com",
    databaseURL: "https://hshacks-investment.firebaseio.com",
    projectId: "hshacks-investment",
    storageBucket: "hshacks-investment.appspot.com",
    messagingSenderId: "334189266034"
};
// Initialize Firebase
// TODO: Replace with your project's customized code snippet
firebase.initializeApp(config);
var db = firebase.firestore();
// Initialize Cloud Firestore through Firebase
getDoc(function(data){
    addData(data)
})
getDoc2(function(data){
    addData2(data);
})
getBalance(function(data){
    addBalance(data);
})
function addBalance(data){
    console.log(data["balance"])
    var ele = document.getElementById("balance")
    ele.innerHTML = "Current Balance: "+data["balance"]
}
function addData(data){
    console.log(data["symbol"])
    console.log("adding data")
    var div = document.getElementById("most_common2");
    var buyprice = data["buyprice"];
    var quantity = data["quantity"];
    var action = data["tradetype"]; 
    
    var row = document.createElement("div");
    row.className="row2";

    var col1 = document.createElement("div");
    col1.className="col-md-3";
    row.appendChild(col1);
    col1.innerHTML= data["symbol"];

    var col2 = document.createElement("div");
    col2.className="col-md-3";
    row.appendChild(col2);
    col2.innerHTML= buyprice;

    var col3 = document.createElement("div");
    col3.className="col-md-3";
    row.appendChild(col3);
    col3.innerHTML= quantity;

    var col4 = document.createElement("div");
    col4.className="col-md-3";
    row.appendChild(col4);
    col4.innerHTML= action;

    div.appendChild(row);    
}

function addData2(data){
    console.log(data["symbol"])
    console.log("adding data")
    var div = document.getElementById("most_common3");
    var buyprice = data["buyprice"];
    var sellprice = data["sellprice"];
    var quantity = data["quantity"];
    var profit = data["profit"];
    var action = data["tradetype"]; 

    
    var row = document.createElement("div");
    row.className="row3";

    var col1 = document.createElement("div");
    col1.className="col-md-2";
    row.appendChild(col1);
    col1.innerHTML= data["symbol"];

    var col2 = document.createElement("div");
    col2.className="col-md-2";
    row.appendChild(col2);
    col2.innerHTML= buyprice;

    var col3 = document.createElement("div");
    col3.className="col-md-2";
    row.appendChild(col3);
    col3.innerHTML= sellprice;

    var col4 = document.createElement("div");
    col4.className="col-md-2";
    row.appendChild(col4);
    col4.innerHTML= quantity;

    var col5 = document.createElement("div");
    col5.className="col-md-2";
    row.appendChild(col5);
    col5.innerHTML= profit;
    if(profit> 0){
        col5.style.background="#99ff99";
    }
    else if(profit<0){
        col5.style.background="#ff9999";
    }

    var col6 = document.createElement("div");
    col6.className="col-md-2";
    row.appendChild(col6);
    col6.innerHTML= action;

    div.appendChild(row); 
}
function getDoc(callback){
    var docRef = db.collection("portfolio").doc("portfolio1").collection("portfolio");
    data = {}
    docRef.get().then(function(querySnapshot) {
        querySnapshot.forEach(function(doc) {
            callback(doc.data()) //doc.data() is dictionary
            // doc.data() is never undefined for query doc snapshots
        });
    });
}
function getDoc2(callback){
    var docRef = db.collection("portfolio").doc("portfolio1").collection("history");
    data = {}
    docRef.get().then(function(querySnapshot) {
        querySnapshot.forEach(function(doc) {
            callback(doc.data()) //doc.data() is dictionary
            // doc.data() is never undefined for query doc snapshots
        });
    });
}
function getBalance(callback){
    console.log("getting balance")
    var docRef = db.collection("portfolio").doc("portfolio1")
    docRef.get().then(function(doc) {
        data = doc.data()
        callback(data)
    })
}
